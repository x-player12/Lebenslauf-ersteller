Name_des_Ansprechpatner = input("Name des Ansprechpatner(In)")
Ihr_Name = input("Ihr Name...?")
Alter = input("Ihr Alter...?")
Sprache1 = input("Welche Sprachen sprechen Sie...?")
Sprache2 = input(" Haben Sie vieleicht eine andere Sprache elernt...?")
Sprache3 = input("Vielleicht eine dritte Sprache...?")
Stadt = input("In welcher Stadt leben Sie...?")
Abschluss = input("Welchen Abschluss haben Sie (Matura Abschluss, Real Abschluss etc.)...?")
derzeit = input("Was besuchen Sie derzeit (Name der Lehrstätte)...?")
stelle = input("Für was möchten Sie sich bewerben (Name der Stelle)...?")
firma = input("Wie lautet der Name des Unternehmens...?")
stelle = input("Für welche Stelle bewerben Sie sich...?")
tele = input("Ihre Telefonnummer...:")
mail = input("Ihre E-Mail...:")
erfahrung = input("Ihre Erfahrung...:")


Ansprechpatner_mänlich = input("Wem schreiben Sie? (Frau oder Mann) ")

if Ansprechpatner_mänlich == "Mann":
    print("Sehr geehrter Herr " + Name_des_Ansprechpatner + " ")
if Ansprechpatner_mänlich == "Frau":
    print("Sehr geehrte Frau "+ Name_des_Ansprechpatner +" ")

print("mein Name ist " + Ihr_Name + "," "derzeit wohne ich in " + Stadt + " und bin " + Alter + " Jahre alt.")
print("Sprachen die ich erlernt habe sind " + Sprache1 + " " + Sprache2 + " " + Sprache3 + ".")
print("Ich habe einen " + Abschluss +" und besuche derzeit " + derzeit + "Ich möchte mich gerne in Ihrer Frima " + firma + " als " + stelle + " bewerben.")
print("Ich bin sehr davon überzeugt Ihren Unternehmen Hilfe zu leisten und Ihre Unternehmensziele zu verwirklichen. ")
print("Vom Unternehmen " + firma + " bin ich schon seit längere Zeit zufriedener Kunde und ich sehe mich qualifiziert als " + stelle + " zu arbeiten. Ich habe Erfahrung als " + erfahrung + " und will mich jetzt Ihrem Unternehmnen widmen")
print("Ich hoffe ich stimme Ihren Vorraussetzungen zu und ebenfalls das ich Ihr Unternehmen helfen kann. Bitte kontaktieren Sie mich unter meiner Telfonnummer: " + tele +  " oder unter meiner E-Mail Adresse: " + mail +"")
print("Mit freundlichen Grüßen " + Ihr_Name + " ")
input("Enter drücken um Pogramm zu schließen")