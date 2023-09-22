from fuzz import check,checkops
from main import  say
from test2 import speech_recog
from intcheck import quant_recog

class CafeOrder:
    def __init__(self):
        self.menu={
  'Raj Kachori': 160.0,
  'Sev Puri': 140.0,
  'Pani Puri - Suji': 65.0,
  'Pani Puri - Atta': 65.0,
  'Bhalla Papdi': 150.0,
  'Dahi Bhalla': 150.0,
  'Aloo Tikki': 115.0,
  'Bhel Puri': 95.0,
  'Papdi Chaat': 150.0,
  'Dhokla Paneer': 190.0,
  'Dhokla Plain': 130.0,
  'Dhokla Sandwich': 190.0,
  'Samosa': 18.0,
  'Kachori Khasta': 18.0,
  'Pyaz Kachori': 38.0,
  'Samosa - Five pcs': 90.0,
  'Pyaz Kachori Plate - Two Pcs': 76.0,
  'Samosa - Two pcs': 36.0,
  'Paneer Pakoda - 2 pcs': 76.0,
  'Paneer Cutlet - 2 Pcs': 72.0,
  'Choley Bhature': 175.0,
  'Pao Bhaji': 175.0,
  'Kachori With Aloo Subji': 105.0,
  'Matar Kulcha': 145.0,
  'Spring Roll': 210.0,
  'Punjabi Chana Kulcha': 150.0,
  'Veg Grill Cheese Sandwich': 185.0,
  'Veg Sandwich': 50.0,
  'Veg Grill Cheese Sandwich With Pepsi': 250.0,
  'Shahi Paneer with Roti & Salad': 280.0,
  'Chole Bhature With Pepsi Can': 220.0,
  'Pao Bhaji with Pepsi Can': 220.0,
  'Paneer Tikka With Pepsi Can': 360.0,
  'Sambhar With Rice': 129.0,
  'Dal Makhani with Rice': 179.0,
  'Aloo Kulcha With Dal And Raita': 240.0,
  'Chole with Rice': 149.0,
  'Onion Kulcha With Dal And Raita': 240.0,
  'Rajma with Rice': 149.0,
  'Paneer Kulcha With Dal And Raita': 250.0,
  'Party Menu for 10pax': 3618.09,
  'Party Menu Plan II': 3618.09,
  'Dal Makhani': 280.0,
  'Dal Tadka': 220.0,
  'Rajma Masala': 220.0,
  'Shahi Paneer': 340.0,
  'Green Salad': 110.0,
  'Masala Channa': 240.0,
  'Paneer Kulcha': 100.0,
  'Papad': 20.0,
  'Raita Boondi': 140.0,
  'Veg. Pulao': 160.0,
  'Special Paneer': 340.0,
  'Paneer Butter Masala': 340.0,
  'Biscuit Plain Khatai 400g': 144.07,
  'Bread Whole Wheat 100% 300g': 60.0,
  'Suji Rusk 600g': 114.29,
  'Chocolate Box 15pcs': 296.0,
  'Special Thali With Tawa Parantha': 275.0,
  'Special Thali with Tandoori Roti': 275.0,
  'South Indian Platter': 350.0,
  'Tandoori Platter': 380.0,
  'Delux Thali': 370.0,
  'Chinese Platter': 330.0,
  'Tandoori Butter Roti': 35.0,
  'Garlic Naan': 90.0,
  'Roti Missi': 60.0,
  'Parantha Pudina': 80.0,
  'Aloo Kulcha': 85.0,
  'Butter Naan': 80.0,
  'Onion Kulcha': 90.0,
  'Paneer Tikka': 320.0,
  'Parantha Lachha': 75.0,
  'Plain Naan': 60.0,
  'Tandoori Aloo': 260.0,
  'Tandoori Roti': 30.0,
  'Veg Seekh Kebab': 260.0,
  'Dosa Butter Masala': 210.0,
  'Uttapam Mix Veg.': 220.0,
  'Idli Sambhar': 140.0,
  'Paneer Dosa': 220.0,
  'Plain Dosa': 150.0,
  'Sada Dosa': 150.0,
  'Dosa Masala': 200.0,
  'Dosa Onion Rawa': 210.0,
  'Dosa Paneer': 240.0,
  'Dosa Plain': 180.0,
  'Uttapam Onion': 220.0,
  'Uttapam Plain': 190.0,
  'Uttapam Tomato': 220.0,
  'Uttapam Onion Tomato': 220.0,
  'Onion Rawa Masala Dosa': 230.0,
  'Dosa Rawa Masala': 220.0,
  'Dosa Onion Plain': 200.0,
  'Dosa Onion Masala': 220.0,
  'Dosa Butter Plain': 190.0,
  'Vada Sambhar': 140.0,
  'Veg Chowmein With Veg Manchurian': 230.0,
  'Veg. Burger': 110.0,
  'Paneer Momos': 160.0,
  'French Fries': 95.0,
  'Chilly Crispy Potato': 180.0,
  'Veg Fried Rice With Veg Manchurian': 230.0,
  'Veg Noodles': 190.0,
  'Chilly Paneer (gravy)': 280.0,
  'Chilly Paneer (dry)': 280.0,
  'Veg Cheese Burger': 125.0,
  'Chowmein With Chilly Paneer': 230.0,
  'Fried Rice With Chilly Paneer': 230.0,
  'Tomato Soup': 110.0,
  'Veg. Fried Rice': 200.0,
  'Veg Sweet Corn Soup': 110.0,
  'Veg. Manchurian (gravy)': 230.0,
  'Pizza Capsicum Tomato': 250.0,
  'Pizza Veg Cheese': 240.0,
  'Pizza Veggie (onion Capsicum Tomato)': 270.0,
  'Lassi Masala': 98.0,
  'Lassi Kesaria': 98.0,
  'Chhach': 75.0,
  'Badam Drink 180 ml': 47.62,
  'Chocolate Drink 180 ml': 47.62,
  'Strawberry Drink 180 ml': 47.62,
  'Mineral Water Bottle 1 Ltr.': 38.1,
  'Can 7 Up': 57.14,
  'Can Pepsi': 57.14,
  'Cold Coffee': 110.0,
  'Pakiza': 45.0,
  'Rasgulla (10 Pcs)': 120.0,
  'Rasmalai - One Pc': 60.0,
  'Pink Sandwich': 45.0,
  'Malai Chap': 45.0,
  'Cham Cham': 45.0,
  'Chena Toast': 45.0,
  'Malai Roll': 58.0,
  'Kalakand': 345.0,
  'Khoya Fruit Cake': 350.0,
  'Boondi Sweet Prasad 250 Gm': 109.52,
  'Lamba Jamun': 290.0,
  'Kaju Lemon': 700.0,
  'Kaju Chabri': 340.0,
  'Khoya Kheer Kadam': 320.0,
  'Soan Halwa 18g': 16.19,
  'Karachi Halwa 30 Gms': 16.19,
  'Gulab Jamun (1 Piece)': 32.0,
  'Kali Rasbhari': 145.0,
  'Lal Rasbhari': 145.0,
  'Besan Laddu Special': 380.0,
  'Lal Jamun': 190.0,
  'Kala Jamun': 145.0,
  'Kaju Dhoda': 270.0,
  'Laddu Gound': 380.0,
  'Shahi Atta Laddu': 380.0,
  'Rasmalai - Two Pcs': 120.0,
  'Gulab Jamun 2 Pc': 60.0,
  'Kaju Burfii': 490.0,
  'Laddu Atta': 260.0,
  'Laddu Besan': 280.0,
  'Laddu Bikaneri': 240.0,
  'Laddu Jodhpuri': 380.0,
  'Laddu Special (Moti Choor)': 290.0,
  'Moong Dal Burfi': 320.0}
        self.order = {}

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")

    def add_to_order(self, item, quantity=1):
        if item in self.menu:
            if item in self.order:
                self.order[item] += quantity
            else:
                self.order[item] = quantity
            print(f"Added {quantity} {item}(s) to your order.")
        else:
            print("Item not found in the menu. Please choose something from the menu.")

    def remove_from_order(self, item, quantity=1):
        if item in self.order:
            if quantity >= self.order[item]:
                del self.order[item]
            else:
                self.order[item] -= quantity
            print(f"Removed {quantity} {item}(s) from your order.")
        else:
            print("Item not found in your order.")

    def calculate_total(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        return total

    def show_order(self):
        print("Your Current Order:")
        for item, quantity in self.order.items():
            print(f"{item.capitalize()}: {quantity}")

    def place_order(self):
        total = self.calculate_total()
        if total > 0:
            print("Your order:")
            self.show_order()
            print(f"Total Price: ${total:.2f}")
            print("Thank you for your order!")
        else:
            print("Your order is empty. Please add items to your order before placing it.")


def main():
    cafe = CafeOrder()

    while True:
        print("\nWelcome to the Cafe!")
        #cafe.display_menu()

        #choice = input("Choose an option (add/remove/modify/checkout/quit): ").strip().lower()
        print("Choose an option (add/remove/modify/checkout/quit): ")
        rec_ops=speech_recog()
        choice = rec_ops.lower().strip()
        print(choice)

        if choice == 'add':
            #item = input("Enter the item you'd like to add: ").strip().lower()
            print("add-sequence")
            item = check(speech_recog())#.strip().lower()
            print(item)
            #quantity = int(input("Enter the quantity: "))
            #print(f"how many {item} do you want?")
            say(f"how many {item} do you want?")
            quantity = quant_recog()
            cafe.add_to_order(item, quantity)
        elif choice == 'remove':
            #item = input("Enter the item you'd like to remove: ").strip().lower()
            item = check(speech_recog())#.strip().lower()
            quantity = int(input("Enter the quantity: "))
            quantity = quant_recog()
            cafe.remove_from_order(item, quantity)
        elif choice == 'checkout':
            cafe.place_order()
            break
        elif choice == 'quit':
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
