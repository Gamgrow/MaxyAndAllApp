
import datetime
import Search_box

hour = int(datetime.datetime.now().hour)
minut = int(datetime.datetime.now().minute)

class wishme():
    def wishme(text):
        print(text)
        print()
        if hour >= 0 and hour <= 12:
            print('good morning sir,\n I am maxi, \nhow may i help you')
            Search_box.speak('good morning sir, I am maxi, \n  how may i help you')

        elif hour >= 12 and hour <= 18:
            print('good afternoon sir, \nI am maxi,  how may i help you')
            Search_box.speak('good afternoon sir, I am maxi,  how may i help you')

        else:
            print('good evening sir,\n I am maxi,  how may i help you')
            Search_box.speak('good evening sir, I am maxi,  how may i help you')