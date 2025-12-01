{
  description = "devshell with Python 3.13 (nixos-unstable) and debugpy for VS Code";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python313.withPackages (
            ps: with ps; [
              debugpy
              numpy
              sortedcontainers
            ]
          ))
        ];

        shellHook = ''
          echo "python -> $(which python) ; python --version -> $(python --version 2>&1)"
        '';
      };
    };
}
