
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

def clear_console():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear_console()
    print("\033[1mBITSAT 2025 Rank & Branch Predictor\033[0m")
    print("-----------------------------------")

    try:
        score = float(input("\nEnter your BITSAT score: "))
        bonus = input("\nDid you attempt bonus questions? (yes/no): ").strip().lower()

        bonus_questions = bonus == "yes"
        predicted_rank = predict_bitsat_rank(score, bonus_questions)
        
        clear_console()
        print("\033[1mResults:\033[0m")
        print("-----------------------------------")
        print(f"\nPredicted BITSAT rank: {predicted_rank}")
        
        # Branch prediction
        eligible_branches = get_eligible_branches(int(score))
        if eligible_branches:
            print("\n\033[1m✅ Eligible branches (2024 cutoffs):\033[0m")
            for branch in eligible_branches:
                print(f"• {branch}")
        else:
            print("\n\033[1m❌ Score below 2024 cutoffs for direct admission\033[0m")
        
        input("\nPress Enter to try again...")
        main()

    except ValueError:
        print("\nInvalid input. Please enter numeric values for score.")
        input("\nPress Enter to try again...")
        main()

if __name__ == "__main__":
    main()
