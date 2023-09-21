from flask import Flask, request, jsonify
import actors
import os

app = Flask(__name__)

@app.route("/perform", methods=["POST"])
def perform_scene():
    try:
        scene = request.json.get("scene")
        director_notes = request.json.get("director_notes")
        actor_types = request.json.get("actor_types", ["classically_trained"] * 4)

        actor_lines = [actors.generate_lines(actor_type, scene, director_notes) for actor_type in actor_types]
        
        actor_output = {f"actor{i+1}": line for i, line in enumerate(actor_lines)}

        return jsonify(actor_output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
