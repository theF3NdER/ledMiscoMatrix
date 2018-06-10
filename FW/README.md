
# Prerequisites

You need to follow this instructions the first time you try to compile a project for this:


The package sources are updated:

```bash
sudo apt-get update
```

We install the required packages (confirm with Y):
```bash
sudo apt-get install gcc make build-essential python-dev git scons swig
```

The audio output must be deactivated. For this we edit the file
```bash
sudo nano /etc/modprobe.d/snd-blacklist.conf
```

Here we add the following line: ```blacklist snd_bcm2835```

Then the file is saved by pressing CTRL + O and CTRL + X closes the editor.

We also need to edit the configuration file:

```bash
sudo nano /boot/config.txt
```

Below are lines with the following content (with Ctrl + W you can search):

	# Enable audio (loads snd_bcm2835)
	dtparam=audio=on

This bottom line is commented out with a hashtag # at the beginning of the line: #dtparam=audio=on

We restart the system
```bash
sudo reboot
``` 

Now we can download the library.

```bash
git clone https://github.com/jgarff/rpi_ws281x
```

In this directory are on the one hand some C files included, which can be easily compiled. The example code for this is easy to understand. In order to use them in Python, we need to compile them:
``bash
cd rpi_ws281x/
sudo scons
```
However, in this tutorial we are mainly interested in the Python variant and therefore switch to the Python folder:
```bash
cd python
```

Here we carry out the installation:
```bash
sudo python setup.py build
sudo python setup.py install
```

Done!

### Adjusting Pinout

Check this website to know which number to put to change pin:
https://pinout.xyz/
