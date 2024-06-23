## Download Portable SVM

<img width="912" alt="image" src="https://github.com/ebanner/Learning/assets/2068912/13e7b7bb-0413-49e7-8edb-6590ddfd8fc9">

## Build scheme

```
cd src
./configure
make
make macosx-app
```

`mit-scheme.app/Contents/Resources/mit-scheme` is the executable

## Spacemacs configuration

```
     (scheme :variables
             scheme-implementations '(mit)
             geiser-mit-binary "/Users/edward/Downloads/mit-scheme-12.1/src/mit-scheme.app/Contents/Resources/mit-scheme"
             geiser-default-implementation 'mit)
```

## Inside Emacs

```
M-x geiser
```

# TODO

I still haven't got it working where I can send scheme code to a Geiser REPL. I always get [an error](https://www.reddit.com/r/emacs/comments/1djld33/cant_send_mitscheme_code_to_geiser_repl/) 😕
