run_panel_plot:
	python3 main.py

install_requirements:
	pip install -r requirements.txt && sudo apt-get update && sudo apt-get install libgeos-dev && pip install https://github.com/matplotlib/basemap/archive/master.zip

formatting:
	safety check
	isort .
	black .
	flake8 .

install_requirements_dev:
	pip install -r requirements_dev.txt

docker_build:
	docker build . -t spatial_plotting

docker_run:
	docker run spatial_plotting

download_basemap:
	wget https://github.com/matplotlib/basemap/archive/master.zip && unzip master.zip 

install_geos:
	cd basemap-master && cd geos-3.3.3 && env GEOS_DIR=/usr/local ./configure && make && make check && make install
# cd basemap-master && cd geos-3.3.3 && ./configure && make && make check && make install

cleanup_basemap:
	rm -rf basemap-master && pip install https://github.com/matplotlib/basemap/archive/master.zip && rm master.zip