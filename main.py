
def predict_bitsat_rank(score, bonus_questions=False):
    """
    Predicts the BITSAT rank based on score.
    
    :param score: Your BITSAT score (integer)
    :param bonus_questions: True if you attempted 12 bonus questions (score out of 426), else False
    :return: Predicted approximate rank
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
    
    # Make sure rank is at least 1
    rank = max(1, int(rank))
    return rank


def main():
    print("BITSAT 2025 Rank Predictor")
    print("---------------------------")
    
    try:
        score = float(input("Enter your BITSAT score: "))
        bonus = input("Did you attempt bonus questions? (yes/no): ").strip().lower()
        
        bonus_questions = bonus == "yes"
        
        predicted_rank = predict_bitsat_rank(score, bonus_questions)
        
        print(f"\nYour predicted BITSAT rank is approximately: {predicted_rank}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for score.")

if __name__ == "__main__":
    main()
