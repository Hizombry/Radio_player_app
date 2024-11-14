{ pkgs }: {
  deps = [
    pkgs.portaudio
    pkgs.libvlc
    pkgs.vlc 
  ];
  python312Packages = with pkgs; [
    python312Packages.pip
  ];
}
