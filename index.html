import random
import time
import os

# 1. विषयों की सूची (सब्जेक्ट वाइज)
SUBJECTS = ["हिंदी", "अंग्रेजी", "सामाजिक विज्ञान", "विज्ञान", "गणित", "संस्कृत"]

class StudentQuiz:
    def __init__(self):
        self.correct = 0
        self.wrong = 0
        self.attempted = 0

    def start_app(self):
        print("--- STUDENT QUIZ PRO 2026 ---")
        for i, sub in enumerate(SUBJECTS, 1):
            print(f"{i}. {sub}")
        
        choice = int(input("\nअपना विषय चुनें (1-6): ")) - 1
        print(f"\n{SUBJECTS[choice]} विषय शुरू हो रहा है...")
        self.play_quiz()

    def play_quiz(self):
        # 15 प्रश्न रैंडम चुनना (500 में से कोई भी)
        for i in range(1, 16):
            print(f"\nप्रश्न {i}: भारत की राजधानी क्या है?") # उदाहरण प्रश्न
            
            # उत्तर शफलिंग (Option Shuffling)
            options = ["नई दिल्ली", "मुंबई", "जयपुर", "कोलकाता"]
            random.shuffle(options)
            
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")
            
            ans = input("\nउत्तर (1-4) या 'S' स्किप / 'Q' सबमिट: ").upper()

            if ans == 'Q': break
            if ans == 'S': continue

            self.attempted += 1
            # 0.5 सेकंड में अगला प्रश्न और रंग लॉजिक (कमेंट्स में)
            if options[int(ans)-1] == "नई दिल्ली":
                print("सही उत्तर! ✅ (Green)")
                self.correct += 1
                time.sleep(0.5) 
            else:
                print("गलत उत्तर! ❌ (Red)")
                self.wrong += 1
                time.sleep(1)

        self.final_result()

    def final_result(self):
        # एक्यूरेसी और छात्र की रैंक
        accuracy = (self.correct / self.attempted * 100) if self.attempted > 0 else 0
        print(f"\n--- रिपोर्ट कार्ड ---")
        print(f"सही: {self.correct} | गलत: {self.wrong}")
        print(f"एक्यूरेसी: {accuracy:.2f}%")
        
        rank = "Rank 1" if accuracy > 80 else "Rank 2" if accuracy > 50 else "Rank 3"
        print(f"आपकी रैंक: {rank}")

if __name__ == "__main__":
    app = StudentQuiz()
    app.start_app()
