# random_cow[.py]

A tiny Python project to keep me busy

## Getting Started

* Clone the repo
* Set the execution permission on the file if you get "Permission Denied" by running:

```
cd $(pwd)/random_cow && sudo chmod +x random_cow.py
```


### Prerequisites

* Python 3.x
* The cowsay program. If you are using Ubuntu, Debian, or a Debian spinoff you can run
```
sudo apt install cowsay -y
```
* to be able to use the cowsay and cowthink commands



### Installing

If you want to be able to run the script as a command from anywhere, copy it to the userspace binaries directory

```
sudo cp ./random_cow.py /usr/bin/random_cow
```

**Be extremely careful when copying into the root filesystem as a superuser! (That means with sudo.) _Never use the -r, -f, or -rf flags of the cp command_ unless you are absolutely sure you know what you are doing.**

_I want a cool ASCII message with a random cow whenever I start my terminal. What do I do?_

Assuming you are using bash:
```
sudo apt update && sudo apt install -y fortune && cd ~ && touch .bash_login && echo "fortune | random_cow" > ./bash_login && echo -e "\n" && cat /etc/issue
```
There are a wide variety of fortune addon packages to choose from, including fortunes in German, Russian, Polish, Spanish, Czech, Slovak, Bulgarian, and even Esperanto. 

_Keep in mind some may be offensive. Packages containing text some may consider offensive are clearly labeled and easily avoided._ 

Browse these packages with the following command:
```
sudo apt update && apt-cache search --names-only fortunes
```

_ASCII art is lame. It's 2018, I own dual 4K monitors, I want something graphical!_

* Check out the **xcowsay** package, although you'll probably still think this whole thing is lame.

## Where are the tests?

I swear I'll write them when I have some time later.

## Built With

* [Sublime Text](https://www.sublimetext.com/) - A sophisticated text editor for code, markup and prose
* [PyCharms](https://www.jetbrains.com/pycharm/) - Python IDE for Professional Developers by JetBrains
* Good old git


## Authors

* **Daniel J Mercurio**  - [GitHub.com/danjmercurio](https://github.com/danjmercurio)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **Tony Monroe**, author of cowsay and cowthink 3.03, &copy;1999
* Many anonymous programmers who contributed to the **fortune** command-line utility, which pairs well with cowsay

