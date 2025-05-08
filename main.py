from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def get_eligible_branches(score):
    branches = [
        # Pilani Campus
        {"campus": "Pilani", "branch": "Computer Science", "cutoff": 330},
        {"campus": "Pilani", "branch": "Mathematics and Computing", "cutoff": 322},
        {"campus": "Pilani", "branch": "Electronics & Communication", "cutoff": 320},
        {"campus": "Pilani", "branch": "Electrical & Electronics", "cutoff": 298},
        {"campus": "Pilani", "branch": "Electronics & Instrumentation", "cutoff": 288},
        {"campus": "Pilani", "branch": "Mechanical", "cutoff": 272},
        {"campus": "Pilani", "branch": "Chemical", "cutoff": 255},
        {"campus": "Pilani", "branch": "Manufacturing", "cutoff": 250},
        {"campus": "Pilani", "branch": "Civil", "cutoff": 245},
        {"campus": "Pilani", "branch": "M.Sc. Economics", "cutoff": 275},
        {"campus": "Pilani", "branch": "M.Sc. Mathematics", "cutoff": 260},
        {"campus": "Pilani", "branch": "M.Sc. Physics", "cutoff": 258},
        {"campus": "Pilani", "branch": "M.Sc. Chemistry", "cutoff": 245},
        {"campus": "Pilani", "branch": "M.Sc. Biological Sciences", "cutoff": 240},
        {"campus": "Pilani", "branch": "B.Pharm", "cutoff": 170},

        # Goa Campus
        {"campus": "Goa", "branch": "Computer Science", "cutoff": 305},
        {"campus": "Goa", "branch": "Mathematics and Computing", "cutoff": 300},
        {"campus": "Goa", "branch": "Electronics & Communication", "cutoff": 292},
        {"campus": "Goa", "branch": "Electrical & Electronics", "cutoff": 285},
        {"campus": "Goa", "branch": "Electronics & Instrumentation", "cutoff": 275},
        {"campus": "Goa", "branch": "Mechanical", "cutoff": 260},
        {"campus": "Goa", "branch": "Chemical", "cutoff": 245},
        {"campus": "Goa", "branch": "M.Sc. Economics", "cutoff": 268},
        {"campus": "Goa", "branch": "M.Sc. Mathematics", "cutoff": 254},
        {"campus": "Goa", "branch": "M.Sc. Physics", "cutoff": 249},
        {"campus": "Goa", "branch": "M.Sc. Chemistry", "cutoff": 240},
        {"campus": "Goa", "branch": "M.Sc. Biological Sciences", "cutoff": 238},

        # Hyderabad Campus
        {"campus": "Hyderabad", "branch": "Computer Science", "cutoff": 302},
        {"campus": "Hyderabad", "branch": "Mathematics and Computing", "cutoff": 298},
        {"campus": "Hyderabad", "branch": "Electronics & Communication", "cutoff": 290},
        {"campus": "Hyderabad", "branch": "Electrical & Electronics", "cutoff": 280},
        {"campus": "Hyderabad", "branch": "Electronics & Instrumentation", "cutoff": 275},
        {"campus": "Hyderabad", "branch": "Mechanical", "cutoff": 258},
        {"campus": "Hyderabad", "branch": "Chemical", "cutoff": 243},
        {"campus": "Hyderabad", "branch": "Civil", "cutoff": 240},
        {"campus": "Hyderabad", "branch": "M.Sc. Economics", "cutoff": 265},
        {"campus": "Hyderabad", "branch": "M.Sc. Mathematics", "cutoff": 251},
        {"campus": "Hyderabad", "branch": "M.Sc. Physics", "cutoff": 250},
        {"campus": "Hyderabad", "branch": "M.Sc. Chemistry", "cutoff": 240},
        {"campus": "Hyderabad", "branch": "M.Sc. Biological Sciences", "cutoff": 238},
        {"campus": "Hyderabad", "branch": "B.Pharm", "cutoff": 165},
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
