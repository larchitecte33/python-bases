class Point:
    # Constructeur
    def __init__(self, x, y, couleur):
        self.__x = x
        self.__y = y
        self.__couleur = couleur

    # Accesseurs et mutateurs
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y



    def deplacer(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    def changer_couleur(self, new_couleur):
        self.__couleur = new_couleur

    def afficher(self):
        print('x = ', self.__x, ', y = ', self.__y, ', couleur = ', self.__couleur)