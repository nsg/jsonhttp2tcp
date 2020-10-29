# jsonhttp2tcp

JavaScript Object Notation Hypertext Transfer Protocol to Transmission Control Protocol translation service :P

## Snap

### Build

Automatic build by build.snapcraft.io, run `snapcraft` to trigger an local build.

### Install and configure

```
sudo snap install jsonhttp2tcp
sudo snap jsonhttp2tcp src-port=8080
sudo snap jsonhttp2tcp dest-port=8081
```

## Docker

### Build

```
sudo docker build . -t nsgb/jsonhttp2tcp
```

### Run and configure

```
sudo docker run -ti -e SRC_PORT=8080 -e DEST_PORT=8081 nsgb/jsonhttp2tcp
```
