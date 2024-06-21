# podman-basic-comands

```
podman      - for directly managing pods and container images (run, stop, start, ps, attach, etc.)
buildah     - for building, pushing and signing container images
skopeo      - for copying, inspecting, deleting and signing images
runc        - for providing containerrun and build features to podman and buildah
crun        - an optional runtime that can be configured and gives greater flexibility, control and security for rootles containers
```
```
images      - template of container - containers can be created through images
pods        - group of containers deployed together on the hos
```
```
podman search httpd                     -> search thru all repositories for image
podman images                           -> list downloaded images 
podman pull docker.io/library/httpd     -> download available image
podman ps -a                            -> list all containters
podman run -dt -p 8080:80/tcp docker.io/library/httpd       -> run container
podman run -dt -p 8081:80/tcp docker.io/library/httpd       -> run container
    -d  -> detached mode
    -t  -> get the tty shell
    -p  -> port mapping [host] : [container] 

podman logs -l                          -> view podman logs
podman stop container-id                -> stop container
podman start container-id               -> start container
podman create --name httpd docker.io/library/httpd          -> create container but don't run/start it 
```