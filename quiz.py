import random
import time
import os

# यह क्लास आपके पूरे ऐप को कंट्रोल करती है
class SuperQuizApp:
    def __init__(self):
        # 1. आपके द्वारा बताए गए 6 विषय
        self.subjects = ["हिंदी", "अंग्रेजी", "सामाजिक विज्ञान", "विज्ञान", "गणित", "संस्कृत"]
        
        # 2. प्रश्न बैंक का ढांचा (इसे आप 500 तक बढ़ा सकते हैं)
        self.db = {sub: self.generate_questions(sub) for sub in self.subjects}
        
        # स्कोरबोर्ड और डेटा
        self.correct = 0
        self.wrong = 0
        self.skipped = 0
        self.total_attempted = 0

    def generate_questions(self, subject):
        """यहाँ हम डेमो के लिए प्रश्न बना रहे हैं, आप असली प्रश्न यहाँ जोड़ सकते हैं"""
        q_list = []
        for i in range(1, 101): # हर विषय में 100 प्रश्न का डेमो
            q_list.append({
                "q": f"{subject} का महत्वपूर्ण प्रश्न संख्या {i}?",
                "options": [f"सही उत्तर {i}", "गलत विकल्प A", "गलत विकल्प B", "गलत विकल्प C"],
                "answer": f"सही उत्तर {i}"
            })
        return q_list

    def start(self):
        print("\n" + "="*30)
        print("   STUDENT QUIZ SYSTEM 2026   ")
        print("="*30)
        
        # विषय-वार प्रश्न होने चाहिए
        print("\nकृपया अपना विषय चुनें:")
        for idx, sub in enumerate(self.subjects, 1):
            print(f"{idx}. {sub}")
        
        try:
            choice = int(input("\nनंबर दर्ज करें (1-6): ")) - 1
            if 0 <= choice < 6:
                selected_sub = self.subjects[choice]
                # 500 (यहाँ 100) में से 15 रैंडम प्रश्न चुनना
                questions = random.sample(self.db[selected_sub], 15)
                self.run_quiz(questions, selected_sub)
            else:
                print("गलत चुनाव!")
        except ValueError:
            print("कृपया सिर्फ नंबर डालें।")

    def run_quiz(self, questions, sub_name):
        print(f"\n--- {sub_name} क्विज़ शुरू हो रहा है ---")
        
        for i, q_data in enumerate(questions, 1):
            print(f"\nप्रगति: {i}/15")
            print(f"प्रश्न: {q_data['q']}")
            
            # उत्तर शफलिंग (Options Shuffling)
            opts = list(q_data['options'])
            random.shuffle(opts)
            
            for idx, opt in enumerate(opts, 1):
                print(f"{idx}. {opt}")
            
            # Skip और Quit का तगड़ा फीचर
            user_input = input("\nआपका उत्तर (1-4) | 'S' स्किप | 'Q' सबमिट: ").upper()

            if user_input == 'Q': break
            if user_input == 'S': 
                self.skipped += 1
                continue

            try:
                selected_opt = opts[int(user_input)-1]
                self.total_attempted += 1
                
                # सही होने पर हरा फीडबैक (प्रिंट के जरिए) और 0.5s टाइमर
                if selected_opt == q_data['answer']:
                    print("सही जवाब! ✅")
                    self.correct += 1
                    time.sleep(0.5) # 0.5 सेकंड में अगला प्रश्न
                else:
                    print(f"गलत! सही उत्तर था: {q_data['answer']} ❌")
                    self.wrong += 1
                    time.sleep(1)
            except:
                print("गलत इनपुट, प्रश्न स्किप हो गया।")

        self.show_report()

    def show_report(self):
        # एक्यूरेसी रिपोर्ट
        total = self.total_attempted if self.total_attempted > 0 else 1
        accuracy = (self.correct / total) * 100
        
        print("\n" + "="*30)
        print("      अंतिम रिपोर्ट कार्ड      ")
        print("="*30)
        print(f"कुल सही: {self.correct}")
        print(f"कुल गलत: {self.wrong}")
        print(f"स्किप किए: {self.skipped}")
        print(f"सटीकता (Accuracy): {accuracy:.2f}%") #
        
        # छात्र की रैंक
        if accuracy >= 90: rank = "प्रथम (Rank 1) 🏆"
        elif accuracy >= 70: rank = "द्वितीय (Rank 2) 🥈"
        else: rank = "तृतीय (Rank 3) 🥉"
        
        print(f"आपकी रैंक: {rank}") #
        print("="*30)

if __name__ == "__main__":
    app = SuperQuizApp()
    app.start()
