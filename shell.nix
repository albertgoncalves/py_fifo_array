with import <nixpkgs> {};
mkShell {
    buildInputs = [
        (python38.withPackages(ps: with ps; [
            flake8
            numpy
        ]))
        shellcheck
    ];
    shellHook = ''
        . .shellhook
    '';
}
