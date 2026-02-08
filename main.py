import json
import os
import time

def clear_screen():
    # Termux/Linux के लिए स्क्रीन साफ़ करना
    os.system('clear')

def load_database(filename):
    """JSON फाइल को स्कैन और लोड करना"""
    if not os.path.exists(filename):
        print(f"❌ Error: {filename} फाइल नहीं मिली!")
        return None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ फाइल पढ़ने में गलती: {e}")
        return None

def run_quiz():
    db_file = 'questions.json'
    data = load_database(db_file)
    
    if not data:
        return

    while True:
        clear_screen()
        print("================================")
        print("   🎓 10th QUIZ PRO (AIO) 🎓   ")
        print("================================")
        
        # JSON से विषयों को स्कैन करके लिस्ट बनाना
        subjects = list(data.keys())
        print("\nतैयारी के लिए विषय चुनें:")
        for i, sub in enumerate(subjects, 1):
            print(f"{i}. {sub}")
        print(f"{len(subjects) + 1}. बाहर निकलें (Exit)")

        try:
            choice = int(input("\nअपना विकल्प चुनें: "))
            
            if choice == len(subjects) + 1:
                print("ऐप बंद हो रहा है... मेहनत जारी रखें!")
                break
            
            selected_sub = subjects[choice - 1]
            questions = data[selected_sub]
            score = 0

            clear_screen()
            print(f"--- {selected_sub} की परीक्षा शुरू ---")
            
            for index, item in enumerate(questions, 1):
                print(f"\nQ{index}: {item['q']}")
                for i, opt in enumerate(item['options'], 1):
                    print(f"  {i}) {opt}")
                
                user_ans = int(input("\nसही विकल्प का नंबर लिखें (1/2/3): "))
                
                if item['options'][user_ans - 1] == item['ans']:
                    print("✅ बहुत बढ़िया! सही जवाब।")
                    score += 1
                else:
                    print(f"❌ गलत! सही जवाब है: {item['ans']}")
                time.sleep(1)

            print("\n" + "="*20)
            print(f"परिणाम: {score}/{len(questions)}")
            print("="*20)
            input("\nमुख्य मेनू पर जाने के लिए Enter दबाएं...")

        except (ValueError, IndexError):
            print("⚠️ कृपया सही नंबर चुनें!")
            time.sleep(2)

if __name__ == "__main__":
    run_quiz()
