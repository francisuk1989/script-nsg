# Return the unit speed
def speed_unit():
    speed_list=[["Kbps","1"],["Mbps","2"],["Gbps","3"],["Tbps","4"]]
    choix="0"
    while choix != "1" and choix != "2" and choix != "3" and choix != "4":
        print(f"Select your Speed Unit")
        print(f"{'|'}{'-'*8}{'|'}{'-'*8}{'|'}")
        print(f"|  Speed | Choice |")
        for c in speed_list:
            print(f"|  {c[0]}  |    {c[1]}   |")
        print(f"{'|'}{'-'*8}{'|'}{'-'*8}{'|'}")
        choix=input(f"| Votre choix ?   |\n{'|'}{'-'*8}{'|'}{'-'*8}{'|'}\n")
    return speed_list[int(choix)-1][0]

#Return the localisation
def info():
    op=input("Please input the operateur name")
    pays=input("Please input the country and the City (if you have the city)\n")
    code_pays=input("Please input the country code (ex: FR for France)\n")
    speed=input("Please input the Server speed (without the speedunit)\n")
    type_server=input("Please input the Server type (type the enter key to skip it)\n")
    url=input("Enter the URL\n")
    return pays, code_pays, speed,type_server,url, op

# Return all info related to the time
def timing():
    repetition=input("enter the number of repetion (default 2)\n") or "2"
    duree=input("enter the duration in sec (just the number,default 60)\n") or "60"
    pause=input("enter the number of sec between test (default 10)\n") or "10"
    concurrence=input("enter the number of concurrent test (default 1)\n") or "1"
    return repetition,duree,pause,concurrence

def create_filename(speed,speedunit,code_pays,operateur,type_server):
    if type_server:
        filename=f"{operateur}_{type_server}_{speed}{speedunit}_{code_pays}.xml"
    else:
        filename=f"{operateur}_{speed}{speedunit}_{code_pays}.xml"
    return filename
def create_name(operateur,type_server,speed,speed_unit,pays):
    if type_server:
        f"{operateur} {type_server} ({speed}{speed_unit}, {pays})"
    else:
        f"{operateur}({speed}{speed_unit}, {pays})"

def create_file(filename,name,repetition,url,duration,pause,concurrence):
    with open(filename,"w") as file:
        file.write(f'<?xml version="1.0" encoding="UTF-8"?><config>\n  <test>\n    <cases>\n      <case>\n        <type>get-http</type>\n        <name>{name}</name>\n        <enabled>true</enabled>\n        <url>{url}</url>\n        <repeat>{repetition}</repeat>\n        <duration>{duration}</duration>\n        <pause>{pause}</pause>\n        <concurrence>{concurrence}</concurrence>\n      </case>\n    </cases>\n  </test>\n</config>')

def main():
    choix="yes"
    while choix != "no" and choix != "No":
        print(f"Creation of the XML File for GetHTTP")
        unit=speed_unit()
        pays,code_pays,speed,type_server,url,op=info()
        repetition,duree,pause,concurrence=timing()
        filename=create_filename(speed,unit,code_pays,op,type_server)
        name=create_name(op,type_server,speed,speed_unit,pays)
        create_file(filename,name,repetition,url,duree,pause,concurrence)
        choix=input("Create a new file ? Yes/No\n")
    print("Bye")

main()