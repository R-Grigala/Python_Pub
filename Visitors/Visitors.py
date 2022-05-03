import matplotlib.pyplot as plt
import pandas as pd

#test aba vnaxot
# წავიკითხოთ მონაცემები excel-ის ფაილიდან
file_location = "data_v.xlsx"
visitor = pd.read_excel(file_location)

value = str( input("Choose which data you need :"
                "\n          Parameters : "
                "\n1) Year_And_Quantity"
                "\n2) Country_And_Transport"
                "\n3) exit"
                "\n:  "))

if value == '1' or value == 'Year_And_Quantity':
    grp_Year = visitor['Year'].groupby(visitor['Year'])
    grp_Year = grp_Year.count()
    y = str(input("Choose which you want:"
            "\n1) All_Year_Together "
            "\n2) Only_One_Year "
            "\n3) exit" 
            "\n:  "))

    if y == '1' or y == 'All_Year_Together':
        diagram_Year = pd.DataFrame(grp_Year)
        x = str( input("Choose which diagram you need :"
            "\n1) bar_diagram"
            "\n2) line_diagram"
            "\n3) pie_diagram"
            "\n4) exit"
            "\n:  "))

        if x == '1' or x == 'bar_diagram':
            grp_Year.plot(kind= 'bar')
            plt.show()
        elif x == '2' or x == 'line_diagram':
            plt.plot(grp_Year, color = 'r')
            plt.show()
        elif x == '3' or x == 'pie_diagram':
            grp_Year.plot(kind= 'pie')
            plt.show()

        elif value == '3' or value == 'exit':
            exit(-1)

    elif y == '2' or y == 'Only_One_Year':
        year_val = input("Enter Year which you want (2002 ...2009... 2020) :    ")
        grp_Year = grp_Year.groupby(['Year']).get_group(int(year_val))
        diagram_Year = pd.DataFrame(grp_Year)

        grp_Year.plot(kind= 'bar')
        plt.show()

    elif value == '3' or value == 'exit':
        exit(-1)

elif value == '2' or value == 'Country_And_Transport':
    grp_Cou_Tra = visitor['Country'].groupby([visitor['Country'],visitor['Transport']])
    grp_Cou_Tra = grp_Cou_Tra.count()

    country_val = input("Enter Country which you want ( First capital letters! ex..( France )):    ")
    grp_Cou_Tra = grp_Cou_Tra.groupby(['Country']).get_group(country_val)
    transport_val = str(input("Enter Transport which you want (Air, Sea , Tunnel ):  "))
    grp_Cou_Tra = grp_Cou_Tra.groupby(['Transport']).get_group(transport_val)

    diagram_Cou_Tra = pd.DataFrame(grp_Cou_Tra)
    diagram_Cou_Tra.plot(kind= 'bar')
    plt.show()

elif value == '3' or value == 'exit':
    exit(-1)
