from functions import (register_user,authenticate_user,get_closing_prices,analyze_closing_prices,save_to_csv,read_from_csv)  #this is to import functions defined in functions.py

"""User Registration and Login:"""
def main():
    print("Welcome to Stock Selection Tool of Malaysian Market! :)")

    while True:
        choice=input("\n1. Register account\n2. Login \n3. Exit\n Choose any option: ")  #user can choose what option they want by entering the number
        if choice == '1': 
            email=input("Enter your email: ").strip()
            password=input("Enter your password: ").strip()
            if register_user(email, password):
                print("Now, you can log in! :)")
        elif choice == '2':
            email=input("Enter your email: ").strip()
            password=input("Enter your password: ").strip()
            if authenticate_user(email, password):
                print("Login successful! :) ")
    
                
                while True:
                    print("\n1. Fetch Stock Data\n2. View Saved Data\n3. Logout") #user can choose what option they want by entering the number, user only can enter one number
                    user_choice = input("Choose an option: ")
                    
                    if user_choice == '1':
                        ticker = input("Enter stock ticker: ").strip()  #user enter the stock ticker
                        start_date = input("Enter start date (YYYY-MM-DD): ").strip() #user enter the start date
                        end_date = input("Enter end date (YYYY-MM-DD): ").strip() #user enter the end date
                        
                        data = get_closing_prices(ticker, start_date, end_date)  #data retrieval
                        if data is not None: #means if there is data, not none means the data is there
                            print("\nClosing Prices:")
                            print(data) #show the data retrieved
                            
                           
                            analysis = analyze_closing_prices(data)  
                            if analysis:                                            #if there is data, so it will show the analysis
                                print("\nAnalysis:")
                                print(f"Average Closing Price: {analysis[0]}")
                                print(f"Percentage Change: {analysis[1]:.2f}%")
                                print(f"Highest Closing Price: {analysis[2]}")
                                print(f"Lowest Closing Price: {analysis[3]}")
                            else:
                                print("Missing data. Analysis could not be performed.") #this will be show if there is no data for the entered ticker and date by user
                            
                            save_option = input("\nSave this analysis? (yes/no): ").strip().lower()  #this is to save the data for data storage, so user can view it again later if they want
                            if save_option == 'yes':                #it will save the data based on the item in the dictionaries
                                interaction_data = {
                                    "email": email,
                                    "ticker": ticker,
                                    "average": analysis[0],
                                    "percentage_change": analysis[1],
                                    "highest": analysis[2],
                                    "lowest": analysis[3]
                                }
                                save_to_csv([interaction_data], "interactions.csv")
               
                    elif user_choice == '2': #the user can see again the stcck prices that they saved before
                        print("\nSaved Data:")
                        read_from_csv("interactions.csv")
                    
                    elif user_choice == '3': #user logout
                        print("Logging out.")
                        break
                    
                    else:
                        print("Invalid choice. Try again.")   #this is for when user enter wrong number
            
            else:
                print("Invalid email or password.")
        
        elif choice == '3':
            print("Thankyou and please come again! :)")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
