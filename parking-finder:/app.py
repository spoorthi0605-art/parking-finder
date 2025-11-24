from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3
import time
import math

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

DB = "parking.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS spots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL,
            longitude REAL,
            address TEXT,
            status TEXT,
            updated_at INTEGER,
            reports INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ------------------------------------------
# Haversine distance in km
# ------------------------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))


# ------------------------------------------
# GET ALL SPOTS
# ------------------------------------------
@app.route("/spots", methods=["GET"])
def get_spots():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, latitude, longitude, address, status, updated_at, reports FROM spots")
    rows = c.fetchall()
    conn.close()

    results = []
    for r in rows:
        results.append({
            "id": r[0],
            "latitude": float(r[1]),
            "longitude": float(r[2]),
            "address": r[3],
            "status": r[4],
            "updated_at": r[5],
            "reports": int(r[6])
        })
    return jsonify(results)


# ------------------------------------------
# ADD / UPDATE A SPOT
# ------------------------------------------
@app.route("/spots", methods=["POST"])
def add_spot():
    data = request.json

    lat = float(data.get("latitude"))
    lon = float(data.get("longitude"))
    status = data.get("status", "occupied")
    address = data.get("address", None)
    now = int(time.time())

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    merge_thresh_km = 0.03  # merge within 30 meters

    c.execute("SELECT id, latitude, longitude FROM spots")
    rows = c.fetchall()

    found_id = None
    for r in rows:
        sid, slat, slon = r
        if haversine(lat, lon, slat, slon) <= merge_thresh_km:
            found_id = sid
            break

    if found_id:
        if address:
            c.execute("""
                UPDATE spots 
                SET status=?, updated_at=?, reports=reports+1, address=? 
                WHERE id=?
            """, (status, now, address, found_id))
        else:
            c.execute("""
                UPDATE spots 
                SET status=?, updated_at=?, reports=reports+1 
                WHERE id=?
            """, (status, now, found_id))

    else:
        c.execute("""
            INSERT INTO spots (latitude, longitude, address, status, updated_at, reports) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (lat, lon, address, status, now, 1))

    conn.commit()
    conn.close()

    return jsonify({"message": "Spot added/updated"}), 201


# ------------------------------------------
# GET NEARBY SPOTS (USED BY THE MODAL)
# ------------------------------------------
@app.route("/near", methods=["GET"])
def near():
    try:
        lat = float(request.args.get("lat"))
        lon = float(request.args.get("lon"))
    except:
        return jsonify({"error": "lat & lon required"}), 400

    radius_km = float(request.args.get("radius", 1.0))

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, latitude, longitude, address, status, updated_at, reports FROM spots")
    rows = c.fetchall()
    conn.close()

    res = []
    for r in rows:
        sid, slat, slon, addr, status, updated, reports = r

        d = haversine(lat, lon, slat, slon)
        if d <= radius_km:

            res.append({
                "id": sid,
                "latitude": float(slat),
                "longitude": float(slon),
                "address": addr if addr else "",
                "status": status,
                "updated_at": updated,
                "reports": int(reports),
                "distance_km": float(round(d, 4))
            })

    res.sort(key=lambda x: x["distance_km"])
    return jsonify(res)


# ------------------------------------------
# VIEW A SINGLE SPOT
# ------------------------------------------
@app.route("/spot/<int:spot_id>", methods=["GET"])
def spot_detail(spot_id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, latitude, longitude, address, status, updated_at, reports FROM spots WHERE id=?", (spot_id,))
    r = c.fetchone()
    conn.close()

    if not r:
        return jsonify({"error": "not found"}), 404

    return jsonify({
        "id": r[0],
        "latitude": float(r[1]),
        "longitude": float(r[2]),
        "address": r[3],
        "status": r[4],
        "updated_at": r[5],
        "reports": int(r[6])
    })


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
