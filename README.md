
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

```
$ cdk déploy -> déploie la stack sur le compte aws ( pensez à modifier app.py) 
```


To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Pensez à modifier

    * app.py pour ajouter le comtpe et la région pour le déploiement 
    * dans s2_list.R la lib paws est utilisée. Des variables d'environnement sont utilisés pour paramétr les infos de conenxion au compte AWS


## Spécificté pour execution du code R 

    * Les fichiers bootstrap.R et runtime.R sont nécessaires à l'execution et doivent etre copiés tel quel
    * le fichier functions.R est l'endroit ou le code va être saisie. L'execution sera lancer dans le Dockerfile via la commande CMD [functions.nom-de-la-fonction]
    * Le dockerfile contient également quelques spécificités : 
        - un fichier bootstrap.sh conçu pour lancer l 'execution du bootstrap.R
        - une  CMD pour lancer la fonction
    * Librairie paws pour envoie du code vers S3 



