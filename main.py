from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def predict_bitsat_rank(score, bonus_questions=False):
    if bonus_questions:
        if score > 390:
            rank = 48.33 - (0.1111 * score)
        else:
            if score >= 307:
                rank = 9772 - (27.23 * score)
            else:
                rank = 54747 - (173.73 * score)
    else:
        if score >= 307:
            rank = 9772 - (27.23 * score)
        else:
            rank = 54747 - (173.73 * score)

    return max(1, int(rank))

def get_eligible_branches(marks):
    branches = [
        {"campus": "Pilani", "branch": "CSE", "cutoff": 327},
        {"campus": "Pilani", "branch": "ECE", "cutoff": 314},
        {"campus": "Pilani", "branch": "EEE", "cutoff": 292},
        {"campus": "Pilani", "branch": "Mechanical", "cutoff": 266},
        {"campus": "Pilani", "branch": "Chemical", "cutoff": 247},
        {"campus": "Pilani", "branch": "Civil", "cutoff": 238},
        {"campus": "Pilani", "branch": "Manufacturing", "cutoff": 243},
        {"campus": "Pilani", "branch": "Mathematics & Computing", "cutoff": 318},
        {"campus": "Goa", "branch": "CSE", "cutoff": 301},
        {"campus": "Goa", "branch": "ECE", "cutoff": 287},
        {"campus": "Goa", "branch": "EEE", "cutoff": 278},
        {"campus": "Goa", "branch": "Mechanical", "cutoff": 254},
        {"campus": "Goa", "branch": "Chemical", "cutoff": 239},
        {"campus": "Goa", "branch": "Mathematics & Computing", "cutoff": 295},
        {"campus": "Hyderabad", "branch": "CSE", "cutoff": 298},
        {"campus": "Hyderabad", "branch": "ECE", "cutoff": 284},
        {"campus": "Hyderabad", "branch": "EEE", "cutoff": 275},
        {"campus": "Hyderabad", "branch": "Mechanical", "cutoff": 251},
        {"campus": "Hyderabad", "branch": "Chemical", "cutoff": 238},
        {"campus": "Hyderabad", "branch": "Civil", "cutoff": 235},
        {"campus": "Hyderabad", "branch": "Mathematics & Computing", "cutoff": 293},
    ]

    eligible = []
    for b in branches:
        if marks >= b["cutoff"]:
            eligible.append(b)
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
    bonus = data['bonus'] == 'true'

    rank = predict_bitsat_rank(score, bonus)
    branches = get_eligible_branches(int(score))

    return jsonify({
        'rank': rank,
        'branches': branches
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)