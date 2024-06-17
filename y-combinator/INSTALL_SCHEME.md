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

I still haven't got it working where I can send scheme code to a Geiser REPL. I always get this error 🤨

```
(+ 1 1)


Error: retort-syntax

;Unbound variable: geiser:eval
;To continue, call RESTART with an option number:
; (RESTART 6) => Specify a value to use instead of geiser:eval.
; (RESTART 5) => Define geiser:eval to a given value.
; (RESTART 4) => Return to read-eval-print level 4.
; (RESTART 3) => Return to read-eval-print level 3.
; (RESTART 2) => Return to read-eval-print level 2.
; (RESTART 1) => Return to read-eval-print level 1.
```
