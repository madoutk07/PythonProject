# PythonProject

## Présentation
Ce projet est une application Python permettant d'accéder au corpus de documents.

## Installation

**Tester la classe Author :**
```shell
Assurez-vous d'avoir Python installé sur votre système.
```

1. Clonez ce dépôt sur votre machine locale.
    ```shell
    git clone https://github.com/madoutk07/PythonProject.git
    ```

2. Ouvrez le projet
    ```shell
    cd PythonProject
    ```

3. Création de l'environnement virtuel:
    ```shell
    python -m venv venv
    ```

4. Activation de l'environnement virtuel:


    **Windows**
    ```shell
    venv\Scripts\activate
    ```


    **MacOS**
    ```shell
     source venv/bin/activate
    ```


6. Installez les dépendances en exécutant la commande suivante:
    ```shell
    pip install -r requirements.txt
    ```

## Utilisation
1. Pour visualiser la documentation, consultez le fichier `index.html` dans le dossier `html/index`.
2. Pour lancer le projet, exécutez la commande suivante:
    ```shell
    python main.py
    ```
3. Pour lancer les tests, exécutez les commandes suivantes:
    **Tester la classe Author :**
    ```shell
    pytest test_Author.py
    ```
    **Tester les documents :**
    ```shell
    pytest test_Document.py
    ```
    **Tester le corpus :**
    ```shell
    pytest test_Corpus.py
    ```
    **Tester le pattern :**
    ```shell
    pytest test_Pattern.py
    ```

4. Une interface notebook est disponible dans le dossier `programme.ipynb` qui vous permettra de créer des corpus avec des mots-clés.

5. Une interface Dash est disponible dans le dossier `Dash_interface.py` qui vous permettra de  tester l'application.

**Note:**
    ```
    Sur le notebook, faites attention à séparer les mots-clés par des virgules.
    ```
