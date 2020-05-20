# This tool allows the user to improve their French writing ability through a quick feedback loop.
# Created by: Daniel Berrones [email: Daniel.A.Berrones@gmail.com]


from random import choice
from time import sleep
import os.path


class FrenchQuestions:
    def __init__(self):
        self.counter = 1
        self.fileCounter = 1

        self.questionContainer = []
        self.answerContainer = []

        self.all = {}

        self.filename = ""
        self.filepath = ""

        self.questions = [
            "Que manges-tu?",
            "Qui frappe à la porte maintenant?",
            "À qui penses-tu?",
            "Chez qui vas tu? Et avec qui?",
            "Sur qui peux-tu compter?",
            "Quand iras-tu te doucher?",
            "Depuis quand est-ce que vous ne l'avez pas vu?",
            "De quoi as-tu besoin?",
            "Maintenant, je fais quoi?",
            "Où vas-tu dormir ce soir?",
            "Pourquoi as-tu peur?",
            "Comment? Je ne vous comprends pas?",
            "Que fais-tu demain?",
            "Est-ce que tu peux dîner avec nous plus tard?",
            "Voulez-vous que je vous prête ce livre?",
            "Avez-vous lu ce livre?",
            "Qui te parle?",
            "Pourquoi elle pleure?",
            "Est-ce que tu m'entends?",
            "Sur qui pouvons-nous compter?",
            "Vous venez d'où?",
            "Quand viendras-tu?",
            "Quel jour sommes-nous?",
            "Qu'est-ce que ça veut dire?",
            "Pourquoi tu as dit cela?",
            "Est-ce que tu m'aimes?",
            "Pourquoi il a beaucoup pleuré ce soir?",
            "Est-ce que tu comprends le français?",
            "Est-ce que tu aimes le chocolat?",
            "Est-ce que tu vas souvent à la plage?",
            "Qui est là?",
            "Que faut-il faire?",
            "Pourquoi es-tu en colère?",
            "Comment est ton chien avec les gens?",
            "Combien ça coûte?",
            "Quel est ton pays préféré?",
            "Qui êtes-vous?",
            "Que voulez-vous faire?",
            "Pourquoi fait-il cela?",
            "Où es-tu?",
            "Où partez-vous en vacances cette année?",
            "Quelle heure est-il s'il te plaît?",
            "Comment s'appelle ton petit chat?",
            "Quel âge as-tu?",
            "Qui a cassé mon portable?",
            "Où est passé mon frère, tu ne l'as pas vu?",
            "Où vas-tu aller?",
            "Quelle est la capitale de la France?",
            "Où habites-tu?",
            "Comment t'appelles-tu?",
            "Que faites-vous ici?",
            "Quel est ton vrai nom?",
            "Quels films aimeriez-vous voir?",
            "Qu'est-ce qui se passe?",
            "Pouvez-vous me donner un morceau de pain, s'il vous plaît?",
            "Peux-tu me conduire à Paris ce soir?",
            "Est-ce que vous auriez une chambre de libre pour la nuit?",
            "Qu'est-ce que Laurent a donné à Marie?",
            "Où est le livre que tu m'as donné?",
            "Depuis quand les enfants jouent-ils dans le jardin?",
            "Avec qui est-ce que je pars en vacances?",
            "Quel musique aimes-tu écouter?",
            "Tu es libre?",
            "Quel temps fait-il?",
            "Quel âge a ton père?",
            "Que fait-tu pour demain?",
            "Que faisons-nous maintenant?",
            "Quel est le métier de ton père?",
            "Qui est-ce qui part?",
            "Partez-vous?",
            "Comment va-t-elle aujourd'hui?",
            "Suis-je en retard pour mon rendez-vous?",
            "Comment vas-tu à Rome?",
            "Comment va ton frère?",
            "Comment va ta mère?",
            "As-tu envie d'aller te promener?",
            "Ai-je envie de parler avec ma mère?",
            "Ont-ils vraiment besoin de manger autant?",
            "Pourquoi ne veux-tu pas m'aider?",
            "Que ferons-nous aujourd'hui?",
            "Quand veux-tu venir?",
            "Est-ce que tu peux me dire pourqoui?",
            "Tu pars quand?",
            "Quand est-ce que tu m'écouteras?",
            "Quand est-ce que tu vas te taire?",
            "Comment vas-tu depuis tout ce temps?",
            "Où es-tu sur la photo, je ne te vois pas?",
            "Que fais-tu ce matin?",
            "Qui veut m'aider?",
            "Qui veut me parler?",
            "Qui aura besoin de faire ça?",
            "Quoi? Je ne t'entends pas!",
            "Qui a pris le téléphone?",
            "Qui a appelé ce matin?",
            "Que se passe-t-il?",
            "Qui a frappé à ta porte?",
            "Quand est-ce que le gâteau sera cuit?",
            "Qu'est-ce qui m'arrive ce soir?",
            "Qui a allumé la radio?",
            "Qui veut dîner ce soir avec nous?",
            "Qui a perdu son chat?",
            "Qui aime nager?",
            "Que veut-elle faire plus tard comme métier?",
            "Quelles langues parlez-vous?",
            "Quelle heure prend-elle le train?",
            "Quelle heure peut-on l'appeler?",
            "Quel est le nom de ta copine?",
            "Qui a mangé le dernier morceau de gâteau?",
            "Quoi de neuf depuis une semaine?",
            "Est-ce que'elles ont des frères?",
            "Que film est-ce que tu préféres?",
            "Est-ce que vous buvez souvent du café?",
            "Pourquoi est-ce qu'elle apprend le français?",
            "Où vont-ils si tôt?",
            "Quand est-ce que tes amis arriveront?",
            "Qui est-ce qui vient se promener avec moi?",
            "A quel moment prenez-vous votre déjeuner?",
            "Que cherches-tu?",
            "Pourquoi as-tu voulu faire cela?",
            "Veux-tu que je m'en aille?",
            "Veux-tu que je te le dise?"]

    def prompt(self):
        #print("\n********************************************************************")
        print("Bienvenue!  Tu es un étudiant vraiment intelligent... c'est vrai?!")
        #print("********************************************************************")
        sleep(1.5)
        print("INSTRUCTIONS:".center(40,"*"))
        print("Respond to these questions as fast as you can.  Do not pay attention to your errors.")
        print("The quick feedback loop maximizes your brain's ability to learn new information.")
        print("\n"*4)
        print("SELECTION MENU".center(40,"*"))
        print("\t(Type '1' to show your responses)")
        print("\t(Type '2' to exit)\n\n")
        sleep(1.5)


    def ask(self):
        for x in self.questions:
            self.randomQuestion = choice(self.questions)
            print("\n" + str(self.counter) + ") " + str(self.randomQuestion))
            self.userAnswer = input("\t>> ")
            if self.userAnswer == "":
                pass
            elif self.userAnswer == "1": #show responses
                print(self.all)
            elif self.userAnswer == "2": #exit question loop
                print("**********************")
                print("\n** SELECTION MENU **")
                print("**********************")
                print()
                print("\nWould you like to save this file?")
                print("1 - Yes")
                print("2 - No")

                self.quitPrompt = int(input("\nEnter number: "))

                #TODO: FINISH CODING FILE SAVE

                # if self.quitPrompt == 2:
                #     print("\n" * 5)
                #     print("Goodbye".center(30, "-"))
                #     break
                # elif self.quitPrompt == 1:
                #     while True:
                #         print("\n\nPlease type a filename: ")
                #         self.filename = input()
                #         print("\n\nPlease type a filepath: ")
                #         self.filepath = input()
                #         print("Filepath does not exist.  Please retype.")
                #         if os.path.exists(self.filepath) == False:
                #             continue
                #         with open(f"{self.filepath}{self.filename}", "w") as f:
                #             for self.k, self.v in self.all.items():
                #                 f.write(
                #                     "Question #{}: ".format(
                #                         self.fileCounter))
                #                 f.write("{} {}\n".format(self.k, self.v))
                #                 self.fileCounter += 1
                #                 print("\n\nThe file was saved successfully.")
                #                 print("Goodbye".center(30, "-"))
                #                 break
            else:
                self.questionContainer = self.questionContainer + [self.randomQuestion]
                self.answerContainer = self.answerContainer + [self.userAnswer]
                self.all = dict(zip(self.questionContainer, self.answerContainer))
                self.counter += 1
                


def main():
    writing = FrenchQuestions()
    writing.prompt()
    writing.ask()


if __name__ == '__main__':
    main()
