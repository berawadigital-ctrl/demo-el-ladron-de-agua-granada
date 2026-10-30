# Contenido de la demo El Ladrón de Agua (Granada) (es/en/fr/de). Hechos de ladrondeagua.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran los apartamentos reales.','en':' Images are illustrations and do not show the actual apartments.','fr':' Les images sont des illustrations et ne montrent pas les appartements réels.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Apartments.'}
H={'es':['Estudio Classic','Estudio Premium','Apartamento Deluxe','Apartamento Exclusive','Penthouse Suite'],
'en':['Classic Studio','Premium Studio','Deluxe Apartment','Exclusive Apartment','Penthouse Suite'],
'fr':['Studio Classic','Studio Premium','Appartement Deluxe','Appartement Exclusive','Penthouse Suite'],
'de':['Studio Classic','Studio Premium','Apartment Deluxe','Apartment Exclusive','Penthouse Suite']}
RD={
'es':['25 m² para 2 personas, en la parte trasera y sin vistas a la Alhambra, con cama de 180 x 200 cm, cocina equipada y ducha.','27 m² para 2 personas, con vistas a la Alhambra, techo de madera, suelos de barro y cama de 160 x 200 cm.','40 m² hasta 4 personas, con vistas a la Carrera del Darro, cama de 180 x 200 cm y sofá cama.','63 m² hasta 6 personas, dos dormitorios y vistas al río Darro y la Torre de la Vela.','65 m² hasta 6 personas en el Torreón, con artesonado mudéjar y vistas a la Alhambra, el Valle del Darro y Plaza Nueva.'],
'en':['25 m² for 2 people, at the back and without Alhambra views, with a 180 x 200 cm bed, equipped kitchen and shower.','27 m² for 2 people, with Alhambra views, wooden ceiling, clay floors and a 160 x 200 cm bed.','40 m² for up to 4 people, overlooking the Carrera del Darro, with a 180 x 200 cm bed and sofa bed.','63 m² for up to 6 people, two bedrooms and views of the river Darro and the Torre de la Vela.','65 m² for up to 6 people in the Tower, with a Mudéjar coffered ceiling and views of the Alhambra, the Darro valley and Plaza Nueva.'],
'fr':['25 m² pour 2 personnes, à l\'arrière et sans vue sur l\'Alhambra, lit de 180 x 200 cm, cuisine équipée et douche.','27 m² pour 2 personnes, vue sur l\'Alhambra, plafond en bois, sols en terre cuite et lit de 160 x 200 cm.','40 m² jusqu\'à 4 personnes, vue sur la Carrera del Darro, lit de 180 x 200 cm et canapé-lit.','63 m² jusqu\'à 6 personnes, deux chambres et vue sur le Darro et la Torre de la Vela.','65 m² jusqu\'à 6 personnes dans la tour, plafond mudéjar à caissons et vue sur l\'Alhambra, la vallée du Darro et la Plaza Nueva.'],
'de':['25 m² für 2 Personen, auf der Rückseite und ohne Alhambra-Blick, mit Bett 180 x 200 cm, Küche und Dusche.','27 m² für 2 Personen, mit Alhambra-Blick, Holzdecke, Tonböden und Bett 160 x 200 cm.','40 m² für bis zu 4 Personen, mit Blick auf die Carrera del Darro, Bett 180 x 200 cm und Schlafsofa.','63 m² für bis zu 6 Personen, zwei Schlafzimmer und Blick auf den Darro und die Torre de la Vela.','65 m² für bis zu 6 Personen im Turm, mit Mudéjar-Kassettendecke und Blick auf die Alhambra, das Darro-Tal und die Plaza Nueva.']}
ART={
'hero':('arches',9401,['#f3e6d4','#e8b27e','#8a3a2a','#4d2a3a','#2c1622']),
'intro':('columns',9402,['#efebe3','#f8f5ef','#8a3a2a','#4d2a3a','#2c1622']),
'r1':('arches',9411,['#f0e5d3','#e3b380','#a6492a','#4d2a3a','#2c1622']),
'r2':('skyline',9412,['#4d2a3a','#e7a568','#f5d5a3','#2c4a3e','#233e33','#162a22']),
'r3':('waves',9413,['#2c4a3e','#edbd83','#f6deb5','#3c6657','#2c4a3e','#1a3028']),
'r4':('hills',9414,['#e6ece5','#f1e9d3','#edbb79','#a7bd9d','#7b9a81','#52735c']),
'r5':('columns',9415,['#edeae2','#f7f4ee','#ab4e2f','#4d2a3a','#2c1622']),
'g1':('skyline',9421,['#4d2a3a','#e3a266','#f4d29f','#2a483c','#213b31','#152820']),
'g2':('arches',9422,['#eee2ce','#dfae7a','#a14526','#4d2a3a','#2c1622']),
'g3':('waves',9423,['#2a483c','#ebb57c','#f5dcb2','#3a6455','#2a483c','#182e26']),
'g4':('hills',9424,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3','r4','r5'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='El Ladrón de Agua · Apartamentos en un palacete del siglo XVI en Granada',see_rooms='Ver los apartamentos',hero_k='Granada · Carrera del Darro',hero_t='Un palacete del siglo XVI a los pies de la Alhambra',hero_s='Apartamentos turísticos en el Albaicín, en la Carrera del Darro.',
 intro_t='Un lugar donde despiertan los sueños',intro_p1='Edificio histórico rehabilitado del siglo XVI que conserva su ala oeste y el Torreón, con techo mudéjar, alfarjes renacentistas y un patio central de columnas toscanas de mármol.',
 intro_p2='Trato familiar y personalizado: check-in automático 24 horas y atención por teléfono y WhatsApp 24 h, los 7 días.',
 stats=['Palacete del siglo XVI','5 tipos de apartamento','Check-in 24 h','WiFi gratis'],nav_rooms='Apartamentos',rooms_t='Los apartamentos',rooms_s='De 2 a 6 personas, todos con cocina equipada.',
 svcs=['Check-in automático 24 horas','Atención por teléfono y WhatsApp 24 h','Consigna para maletas y bicicleta','Ascensor','Lavadora y secadora','Cuna y trona gratis bajo petición'],
 around_s='En el Albaicín, Patrimonio de la Humanidad: la Alhambra, el Sacromonte y la Catedral, todo accesible a pie.',
 loc_p='Carrera del Darro 13 · 18010 Granada, en el corazón del Albaicín, a los pies de la Alhambra.',
 chips=['¿Qué apartamentos tenéis?','¿Hay parking?','¿A qué hora es el check-in?','¿Puedo cancelar?']),
'en':dict(title='El Ladrón de Agua · Apartments in a 16th-century palace in Granada',see_rooms='See the apartments',hero_k='Granada · Carrera del Darro',hero_t='A 16th-century palace at the foot of the Alhambra',hero_s='Tourist apartments in the Albaicín, on the Carrera del Darro.',
 intro_t='A place where dreams awaken',intro_p1='A restored 16th-century building that keeps its west wing and the Tower, with a Mudéjar ceiling, Renaissance wooden ceilings and a central courtyard with Tuscan marble columns.',
 intro_p2='Friendly, personal service: automatic 24-hour check-in and phone and WhatsApp support 24/7.',
 stats=['16th-century palace','5 apartment types','24 h check-in','Free WiFi'],nav_rooms='Apartments',rooms_t='The apartments',rooms_s='For 2 to 6 people, all with an equipped kitchen.',
 svcs=['Automatic 24-hour check-in','Phone and WhatsApp support 24/7','Luggage and bicycle storage','Lift','Washer and dryer','Free cot and high chair on request'],
 around_s='In the Albaicín, a World Heritage Site: the Alhambra, the Sacromonte and the Cathedral, all within walking distance.',
 loc_p='Carrera del Darro 13 · 18010 Granada, in the heart of the Albaicín, at the foot of the Alhambra.',
 chips=['Which apartments do you have?','Is there parking?','What time is check-in?','Can I cancel?']),
'fr':dict(title='El Ladrón de Agua · Appartements dans un palais du XVIe siècle à Grenade',see_rooms='Voir les appartements',hero_k='Grenade · Carrera del Darro',hero_t='Un palais du XVIe siècle au pied de l\'Alhambra',hero_s='Appartements touristiques dans l\'Albaicín, sur la Carrera del Darro.',
 intro_t='Un lieu où s\'éveillent les rêves',intro_p1='Un bâtiment historique du XVIe siècle restauré, qui conserve son aile ouest et la tour, avec plafond mudéjar, plafonds Renaissance et patio central aux colonnes toscanes en marbre.',
 intro_p2='Un accueil familial et personnalisé : check-in automatique 24 h/24 et assistance par téléphone et WhatsApp 24 h/24, 7 j/7.',
 stats=['Palais du XVIe siècle','5 types d\'appartement','Check-in 24 h/24','WiFi gratuit'],nav_rooms='Appartements',rooms_t='Les appartements',rooms_s='De 2 à 6 personnes, tous avec cuisine équipée.',
 svcs=['Check-in automatique 24 h/24','Assistance téléphone et WhatsApp 24 h/24','Bagagerie et local à vélos','Ascenseur','Lave-linge et sèche-linge','Lit bébé et chaise haute gratuits sur demande'],
 around_s='Dans l\'Albaicín, classé au patrimoine mondial : l\'Alhambra, le Sacromonte et la cathédrale, tout à pied.',
 loc_p='Carrera del Darro 13 · 18010 Grenade, au cœur de l\'Albaicín, au pied de l\'Alhambra.',
 chips=['Quels appartements avez-vous ?','Y a-t-il un parking ?','À quelle heure est le check-in ?','Puis-je annuler ?']),
'de':dict(title='El Ladrón de Agua · Apartments in einem Palast aus dem 16. Jahrhundert in Granada',see_rooms='Apartments ansehen',hero_k='Granada · Carrera del Darro',hero_t='Ein Palast aus dem 16. Jahrhundert zu Füßen der Alhambra',hero_s='Ferienapartments im Albaicín, an der Carrera del Darro.',
 intro_t='Ein Ort, an dem Träume erwachen',intro_p1='Ein restauriertes historisches Gebäude aus dem 16. Jahrhundert mit erhaltenem Westflügel und Turm, Mudéjar-Decke, Renaissance-Holzdecken und einem Innenhof mit toskanischen Marmorsäulen.',
 intro_p2='Familiärer, persönlicher Service: automatischer Check-in rund um die Uhr und Betreuung per Telefon und WhatsApp 24/7.',
 stats=['Palast aus dem 16. Jh.','5 Apartmenttypen','Check-in 24 h','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Die Apartments',rooms_s='Für 2 bis 6 Personen, alle mit ausgestatteter Küche.',
 svcs=['Automatischer Check-in rund um die Uhr','Betreuung per Telefon und WhatsApp 24/7','Gepäck- und Fahrradaufbewahrung','Aufzug','Waschmaschine und Trockner','Kinderbett und Hochstuhl gratis auf Anfrage'],
 around_s='Im Albaicín, Welterbe der UNESCO: Alhambra, Sacromonte und Kathedrale, alles zu Fuß erreichbar.',
 loc_p='Carrera del Darro 13 · 18010 Granada, im Herzen des Albaicín, zu Füßen der Alhambra.',
 chips=['Welche Apartments gibt es?','Gibt es einen Parkplatz?','Wann ist der Check-in?','Kann ich stornieren?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://www.ladrondeagua.com/{l}/book'
BOOK=dict(mode='engine',url={l:RB.format(l=l) for l in ('es','en','fr','de')})
D=dict(name='El Ladrón de Agua',ac='#4d2a3a',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=['Alhambra','Sacromonte'],foot=FOOT,
 address='Carrera del Darro 13 · 18010 Granada',phones=['+34 660 688 593'],emails=['info@ladrondeagua.com'],maps='El Ladrón de Agua Palacete, Carrera del Darro 13, Granada',t=T)
META=dict(repo='demo-el-ladron-de-agua-granada',name='El Ladrón de Agua',legal_name='Poesía y Alegría',registry_ids=['NIF B18990176','RTA A/GR/00450'],
 url='https://www.ladrondeagua.com/',domain='ladrondeagua.com',municipality='Granada',province='Granada',sector='apartamentos turísticos en un palacete del siglo XVI en el Albaicín (Granada)',
 read_at='2026-10-30T06:54:00+01:00',created_at='2026-10-30T06:54:00+01:00',built_at='2026-10-30T07:05:00+01:00',audit_date='2026-10-30T06:47:05+01:00',
 rating=dict(value=4.5,coincide=['telefono','web'],date='2026-10-29T11:02:43+01:00',url='https://www.google.com/maps/place/El+Ladr%C3%B3n+de+Agua+Palacete/@37.1779834,-3.5940639,17z/data=!4m9!3m8!1s0xd71fcb888852e75:0x9117cb990da54f13!5m2!4m1!1i2!8m2!3d37.1779834!4d-3.5940639!16s%2Fg%2F1trszc3y'),
 book=dict(mode='engine',url=RB.format(l='es'),note='motor de reservas real de su web (/book), HTTP 200 comprobado el 30/10/2026 en es/en/fr/de.'),first_of_type=None)
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Tenéis algo para seis personas?','K02'),('¿Cuál tiene vistas a la Alhambra?','K03'),('¿A qué hora es el check-in?','K04'),('¿Hay parking?','K05'),('¿Puedo cancelar?','K06'),('¿Tenéis cuna para el bebé?','K07'),('¿Hay wifi?','K08'),('¿Dónde está?','K09'),('¿Cómo reservo?','K10'),('¿Podéis confirmarme disponibilidad para mañana?','K10'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which apartments do you have?','K01'),('Do you have anything for six people?','K02'),('Which one has Alhambra views?','K03'),('What time is check-in?','K04'),('Is there parking?','K05'),('Can I cancel?','K06'),('Do you have a cot for the baby?','K07'),('Is there wifi?','K08'),('Where is it?','K09'),('How do I book?','K10'),('Can you confirm availability for tomorrow?','K10'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Avez-vous quelque chose pour six personnes ?','K02'),('Lequel a vue sur l\'Alhambra ?','K03'),('À quelle heure est le check-in ?','K04'),('Y a-t-il un parking ?','K05'),('Puis-je annuler ?','K06'),('Avez-vous un lit bébé ?','K07'),('Y a-t-il le wifi ?','K08'),('Où est-ce ?','K09'),('Comment réserver ?','K10'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K10'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Haben Sie etwas für sechs Personen?','K02'),('Welches hat Blick auf die Alhambra?','K03'),('Wann ist der Check-in?','K04'),('Gibt es einen Parkplatz?','K05'),('Kann ich stornieren?','K06'),('Gibt es ein Kinderbett für das Baby?','K07'),('Gibt es WLAN?','K08'),('Wo liegt es?','K09'),('Wie kann ich buchen?','K10'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K10'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
