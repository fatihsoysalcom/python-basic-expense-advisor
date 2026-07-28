# main.py

def run_budget_advisor():
    """
    This function simulates a very basic budget advisor.
    It demonstrates fundamental programming concepts like:
    - User input
    - Variables
    - Type conversion
    - Conditional logic (if/elif/else)
    - Output
    """
    print("Merhaba! Basit Bütçe Danışmanına Hoş Geldiniz.") # Welcome message in Turkish
    print("Welcome to the Simple Budget Advisor!")

    try:
        # Get expense amount from the user
        # Bu kısım, kullanıcıdan sayısal bir değer (harcama miktarı) almayı gösterir.
        # This part demonstrates getting a numerical value (expense amount) from the user.
        amount_str = input("Lütfen harcama miktarını girin (örn: 50.75): ")
        amount = float(amount_str)

        # Get expense category from the user
        # Bu kısım, kullanıcıdan metinsel bir değer (harcama kategorisi) almayı gösterir.
        # This part demonstrates getting a text value (expense category) from the user.
        category = input("Lütfen harcama kategorisini girin (örn: gıda, ulaşım, eğlence, diğer): ").lower()

        # Define some simple budget thresholds for demonstration
        # Gerçek dünya çözümlerinde bu eşikler daha karmaşık olabilir.
        # In real-world solutions, these thresholds could be more complex.
        thresholds = {
            "gıda": 100.0,
            "ulaşım": 50.0,
            "eğlence": 75.0,
            "diğer": 120.0
        }

        # Apply conditional logic based on category and amount
        # Bu kısım, programlamanın temel taşlarından biri olan koşullu mantığı (if/elif/else) kullanır.
        # Farklı durumlara göre farklı çıktılar üretmeyi sağlar.
        # This part uses conditional logic (if/elif/else), one of the cornerstones of programming.
        # It allows producing different outputs based on different conditions.
        if category in thresholds:
            category_threshold = thresholds[category]
            if amount > category_threshold:
                print(f"\nUyarı: {category.capitalize()} kategorisindeki {amount:.2f} TL harcamanız, ortalama eşiğin ({category_threshold:.2f} TL) üzerindedir. Dikkatli olun!")
                print(f"Warning: Your {amount:.2f} TL expense in '{category}' category is above the average threshold ({category_threshold:.2f} TL). Be careful!")
            else:
                print(f"\nBilgi: {category.capitalize()} kategorisindeki {amount:.2f} TL harcamanız, ortalama eşiğin ({category_threshold:.2f} TL) altındadır. İyi yönetim!")
                print(f"Info: Your {amount:.2f} TL expense in '{category}' category is below the average threshold ({category_threshold:.2f} TL). Good management!")
        else:
            print(f"\nBilgi: '{category}' kategorisi için belirli bir eşik tanımlanmamıştır. Harcamanız: {amount:.2f} TL.")
            print(f"Info: No specific threshold defined for '{category}' category. Your expense: {amount:.2f} TL.")

    except ValueError:
        # Error handling for invalid number input
        # Hata yönetimi, programın beklenmedik durumlarda çökmesini engeller ve kullanıcıya bilgi verir.
        # Error handling prevents the program from crashing in unexpected situations and informs the user.
        print("\nHata: Geçersiz miktar girdiniz. Lütfen sadece sayısal değerler kullanın (örn: 50.75).")
        print("Error: Invalid amount entered. Please use only numerical values (e.g., 50.75).")
    except Exception as e:
        print(f"\nBeklenmeyen bir hata oluştu: {e}")
        print(f"An unexpected error occurred: {e}")

    print("\nBütçe danışmanı sona erdi. İyi günler!")
    print("Budget advisor finished. Have a good day!")

if __name__ == "__main__":
    run_budget_advisor()
