cities_str = 'Aberdeen Ashford Aylesbury Banbury Bangor Barnsley Barrow-in-Furness Barry Basildon Basingstoke Bath Bebington Bedford Beeston Belfast Birkenhead Birmingham Blackburn Blackpool Bloxwich Bognor_Regis Bolton Bootle Bournemouth Bracknell Bradford Brentwood Bridgend Brighton_and_Hove Bristol Burnley Burton_upon_Trent Bury Cambridge Cannock Canterbury Cardiff Carlisle Carlton Chatham Chelmsford Cheltenham Chester Chesterfield Clacton-on-Sea Colchester Corby Coventry Craigavon Crawley Crewe Crosby Cumbernauld Darlington	Dartford Derby Derry Dewsbury Doncaster Dudley Dundee Dunfermline Durham Eastbourne East Kilbride	Edinburgh Ellesmere Port Esher Exeter Farnborough Folkestone Gateshead Gillingham Glasgow Gloucester Gosport Gravesend Grimsby Guildford Halesowen Halifax Hamilton	Harlow Harrogate Hartlepool Hastings Hemel Hempstead Hereford High Wycombe Hinckley Horsham Huddersfield Huyton with Roby Ipswich Kettering Kidderminster Kingston_upon_Hull Kingswinford Kingswood Kirkcaldy Lancaster Leeds Leicester Lincoln Lisburn Liverpool Livingston London Loughborough Lowestoft Luton Macclesfield Maidenhead Maidstone Manchester Mansfield Margate Middlesbrough Milton_Keynes Newcastle_upon_Tyne Newcastle-under-Lyme Newport Newtownabbey Northampton Norwich Nottingham Nuneaton Oldham Oxford Paignton Paisley Peterborough Plymouth Poole Portsmouth Preston Reading Redditch Rochdale Rochester Rotherham Royal_Leamington_Spa Royal_Sutton_Coldfield Royal_Tunbridge_Wells	Rugby Runcorn Sale Salford Scarborough Scunthorpe Sheffield Shrewsbury Sittingbourne Slough Smethwick Solihull Southampton Southend-on-Sea Southport South_Shields Stafford St_Albans Stevenage	St_Helens Stockport Stockton-on-Tees Stoke-on-Trent Stourbridge Sunderland Swansea Swindon Tamworth Taunton Telford Thundersley Torquay Tynemouth Wakefield Wallasey Walsall Warrington Washington Watford Wellingborough Welwyn_Garden_City West_Bromwich Weston-super-Mare Weymouth Widnes Wigan Woking Wokingham	Wolverhampton Worcester Worthing Wythenshawe Yeovil York'
#превращаем список в массив и разделяем по проблеу
import random
cities_list = cities_str.split()
user_cities = [True for i in range(len(cities_list))]
def player(last_city):
    city = input('Enter a city: ').titel()
    if city == 'Q':
        return 'computer'
    if checking(city,last_city):
        user_cities[cities_list.index(city)] = False
        return city #если правда то возвращает город (пишет его)
    return player()
def computer(last_city):
    for i in range(len(cities_list)): #проиндексировали каждый город
        if cities_list[i][0].lower() == last_city[-1]:
            if user_cities[i]:
                user_cities[i] = False
                print(f'-{cities_list[i]}')
                return cities_list[i]
    return 'player'
def checking(city, last_city):
    if city not in cities_list: #если нету в списке то If из плеера фелс то это как елиф в плеере
        print('Nvalid city')
        return False
    elif city[0] != last_city[-1]:
        print('Invalid Latter')
    elif not user_cities[cities_list.index()]: #если индекс города в с списке городов есть не тру(фолс) то пишет что уже был
        print('This city has been used')
        return False
    return True
#блок для логики игры
def game():
    computer_city = random.choice(cities_list)
    while True: #бесконечный цикл последовательности игры
        player_city = player(compurt_city) #пишем переменную которая запоминаеит что было в плеере т.е. что в плеере был город котрый прошел проверку и что это за город
        if player_city == 'computer':
            print('Computer win!')
            break
        compurt_city = computer(player_city)
        if compurt_city == 'player':
            print('Player Win!')
            break

