# Install Python py-image-recognize

## Activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

## Install requirements

```bash
pip install -r requirements.txt
```

__Install Nvidia Tensor :__
pip install --no-cache nvidia-tensorrt --index-url https://pypi.ngc.nvidia.com/

__Install PyTorch :__
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt

## Launch dev project

```bash
uvicorn app:app --reload
```

## Launch prod project with docker

```bash
docker build -t py-image-recognize .
docker run --rm -ti -p 8484:8484 py-image-recognize
```
