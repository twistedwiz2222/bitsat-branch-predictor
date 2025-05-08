from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def get_eligible_branches(score):
    branches = [
        # Pilani Campus
        {"campus": "Pilani", "branch": "Computer Science", "cutoff": 327},
        {"campus": "Pilani", "branch": "Mathematics and Computing", "cutoff": 318},
        {"campus": "Pilani", "branch": "Electronics & Communication", "cutoff": 314},
        {"campus": "Pilani", "branch": "Electrical & Electronics", "cutoff": 292},
        {"campus": "Pilani", "branch": "Electronics & Instrumentation", "cutoff": 282},
        {"campus": "Pilani", "branch": "Mechanical", "cutoff": 266},
        {"campus": "Pilani", "branch": "Chemical", "cutoff": 247},
        {"campus": "Pilani", "branch": "Manufacturing", "cutoff": 243},
        {"campus": "Pilani", "branch": "Civil", "cutoff": 238},
        {"campus": "Pilani", "branch": "M.Sc. Economics", "cutoff": 271},
        {"campus": "Pilani", "branch": "M.Sc. Mathematics", "cutoff": 256},
        {"campus": "Pilani", "branch": "M.Sc. Physics", "cutoff": 254},
        {"campus": "Pilani", "branch": "M.Sc. Chemistry", "cutoff": 241},
        {"campus": "Pilani", "branch": "M.Sc. Biological Sciences", "cutoff": 236},
        {"campus": "Pilani", "branch": "B.Pharm", "cutoff": 165},

        # Goa Campus
        {"campus": "Goa", "branch": "Computer Science", "cutoff": 301},
        {"campus": "Goa", "branch": "Mathematics and Computing", "cutoff": 295},
        {"campus": "Goa", "branch": "Electronics & Communication", "cutoff": 287},
        {"campus": "Goa", "branch": "Electrical & Electronics", "cutoff": 278},
        {"campus": "Goa", "branch": "Electronics & Instrumentation", "cutoff": 270},
        {"campus": "Goa", "branch": "Mechanical", "cutoff": 254},
        {"campus": "Goa", "branch": "Chemical", "cutoff": 239},
        {"campus": "Goa", "branch": "M.Sc. Economics", "cutoff": 263},
        {"campus": "Goa", "branch": "M.Sc. Mathematics", "cutoff": 249},
        {"campus": "Goa", "branch": "M.Sc. Physics", "cutoff": 248},
        {"campus": "Goa", "branch": "M.Sc. Chemistry", "cutoff": 236},
        {"campus": "Goa", "branch": "M.Sc. Biological Sciences", "cutoff": 234},

        # Hyderabad Campus
        {"campus": "Hyderabad", "branch": "Computer Science", "cutoff": 298},
        {"campus": "Hyderabad", "branch": "Mathematics and Computing", "cutoff": 293},
        {"campus": "Hyderabad", "branch": "Electronics & Communication", "cutoff": 284},
        {"campus": "Hyderabad", "branch": "Electrical & Electronics", "cutoff": 275},
        {"campus": "Hyderabad", "branch": "Electronics & Instrumentation", "cutoff": 270},
        {"campus": "Hyderabad", "branch": "Mechanical", "cutoff": 251},
        {"campus": "Hyderabad", "branch": "Chemical", "cutoff": 238},
        {"campus": "Hyderabad", "branch": "Civil", "cutoff": 235},
        {"campus": "Hyderabad", "branch": "M.Sc. Economics", "cutoff": 261},
        {"campus": "Hyderabad", "branch": "M.Sc. Mathematics", "cutoff": 247},
        {"campus": "Hyderabad", "branch": "M.Sc. Physics", "cutoff": 245},
        {"campus": "Hyderabad", "branch": "M.Sc. Chemistry", "cutoff": 235},
        {"campus": "Hyderabad", "branch": "M.Sc. Biological Sciences", "cutoff": 234},
        {"campus": "Hyderabad", "branch": "B.Pharm", "cutoff": 161},
    ]

    eligible = []
    for b in branches:
        if score >= b["cutoff"]:
            eligible.append(b)
    
    # Sort by cutoff in descending order (highest cutoff first)
    eligible.sort(key=lambda x: x["cutoff"], reverse=True)
    return eligible


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    score = float(data['score'])

    branches = get_eligible_branches(int(score))

    return jsonify({'branches': branches})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
