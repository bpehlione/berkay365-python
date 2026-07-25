name = input ("Adın nedir? ").strip().title()  # Get the user's name, remove whitespace, and capitalize it
print(f"Merhaba, {name}!")  # Greet the user with their name")
age= int (input("Yaşınızı giriniz: "))  # Get the user's age and convert it to an integer
print(f"Senin yaşın {age}")  # Print the user's age
age_in_next_year = age + 1  # Calculate the user's age next year
print(f"Gelecek yıl senin yaşın {age_in_next_year}")  # Print the user's age next year
age_in_number_of_years = int(input("Kaç yıl sonra yaşını öğrenmek istiyorsun? "))  # Get the number of years to calculate
future_age = age + age_in_number_of_years  # Calculate the user's age in the specified number of years
print(f"{age_in_number_of_years} yıl sonra senin yaşın {future_age} olacak")  # Print the user's age
favorite_number = int(input("En sevdiğin sayıyı gir: "))  # Get the user's favorite number and convert it to an integer
print(f"Senin en sevdiğin sayı {favorite_number}")  # Print the user's favorite number
print(f"Sayının karesi: {favorite_number **2}")  # Print the square of the user's favorite number
print(f"Sayının küpü: {favorite_number **3}")  # Print the cube of the user's favorite number