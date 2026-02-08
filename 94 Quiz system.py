# 17.5 Quiz system
def quiz_system():
    questions = [
        {"q": "What is the capital of France?", "a": "Paris"},
        {"q": "What is 2 + 2?", "a": "4"},
        {"q": "What is the largest planet?", "a": "Jupiter"}
    ]
    
    score = 0
    
    print("--- Quiz Time! ---")
    for i, item in enumerate(questions, 1):
        print(f"\nQ{i}: {item['q']}")
        answer = input("Your answer: ")
        
        if answer.lower() == item['a'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {item['a']}")
    
    print(f"\nYour score: {score}/{len(questions)}")
