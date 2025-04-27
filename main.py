
def predict_bitsat_rank(score, bonus_questions=False):
    """
    Predicts the BITSAT rank based on score.
    """
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
    """
    Returns list of eligible branches based on BITSAT marks
    """
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
    
    return [f'{b["campus"]} - {b["branch"]}' for b in branches if marks >= b["cutoff"]]

def main():
    print("BITSAT 2025 Rank & Branch Predictor")
    print("-----------------------------------")

    try:
        score = float(input("Enter your BITSAT score: "))
        bonus = input("Did you attempt bonus questions? (yes/no): ").strip().lower()

        bonus_questions = bonus == "yes"
        predicted_rank = predict_bitsat_rank(score, bonus_questions)
        
        print(f"\nYour predicted BITSAT rank is approximately: {predicted_rank}")
        
        # Branch prediction
        eligible_branches = get_eligible_branches(int(score))
        if eligible_branches:
            print("\n✅ Based on 2024 cutoffs, you may be eligible for:")
            for branch in eligible_branches:
                print(branch)
        else:
            print("\n❌ Score below 2024 cutoffs for direct admission")

    except ValueError:
        print("Invalid input. Please enter numeric values for score.")

if __name__ == "__main__":
    main()
