%define _enable_debug_packages %{nil}
%define debug_package %{nil}

# We want possibility to install 1.6, 1.9 and possibly other versions
%define oname epsxe
%define major 1.9
%define minor 0

Summary:	Sony PlayStation emulator
Name:		%{oname}%{major}
Version:	%{major}.%{minor}
Release:	4
License:	Freeware
Group:		Emulators
Url:		http://www.epsxe.com
Source0:	%{oname}190lin.zip
Source1:	%{oname}-%{major}-plugins.tar.bz2
Source2:	%{oname}%{major}-start
ExclusiveArch:	%{ix86}
# Not auto-detected but listed in epsxe_linux_en.txt, really ugly way...
Requires:	libasound.so.2
Requires:	libasyncns.so.0
Requires:	libatk-1.0.so.0
Requires:	libcaca.so.0
Requires:	libcairo.so.2
Requires:	libdbus-1.so.3
Requires:	libdl.so.2
Requires:	libexpat.so.1
Requires:	libFLAC.so.8
Requires:	libfontconfig.so.1
Requires:	libfreetype.so.6
Requires:	libgdk_pixbuf-2.0.so.0
Requires:	libgdk-x11-2.0.so.0
Requires:	libgio-2.0.so.0
Requires:	libglib-2.0.so.0
Requires:	libgmodule-2.0.so.0
Requires:	libgobject-2.0.so.0
Requires:	libgthread-2.0.so.0
Requires:	libgtk-x11-2.0.so.0
Requires:	libjson.so.0
Requires:	libm.so.6
Requires:	libncurses.so.5
Requires:	libncursesw.so.6
Requires:	libnsl.so.1
Requires:	libogg.so.0
Requires:	libpango-1.0.so.0
Requires:	libpangocairo-1.0.so.0
Requires:	libpangoft2-1.0.so.0
Requires:	libpixman-1.so.0
Requires:	libpng12.so.0
Requires:	libpthread.so.0
Requires:	libpulse-simple.so.0
Requires:	libpulse.so.0
Requires:	libSDL-1.2.so.0
Requires:	libSDL_ttf-2.0.so.0
Requires:	libslang.so.2
Requires:	libsndfile.so.1
Requires:	libtinfo.so.5
Requires:	libvorbisenc.so.2
Requires:	libvorbis.so.0
Requires:	libwrap.so.0
Requires:	libX11.so.6
Requires:	libXau.so.6
Requires:	libxcb-render.so.0
Requires:	libxcb-shm.so.0
Requires:	libxcb.so.1
Requires:	libXcomposite.so.1
Requires:	libXcursor.so.1
Requires:	libXdamage.so.1
Requires:	libXdmcp.so.6
Requires:	libXext.so.6
Requires:	libXfixes.so.3
Requires:	libXinerama.so.1
Requires:	libXi.so.6
Requires:	libXrandr.so.2
Requires:	libXrender.so.1
Requires:	libz.so.1

%description
Great Sony PlayStation emulator. Requires a BIOS image. Includes
the best external plugins (in addition to internal ones):

GPU P.E.Op.S. MesaGL 1.78
GPU P.E.Op.S. SoftX 1.18
GPU Pete's XGL2 2.9
SPU P.E.Op.S. OSS 1.9

%prep
%setup -q -c -a1

%build

%install
install -D -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{oname}%{major}-start
install -D -m 0644 %{oname}.png %{buildroot}%{_datadir}/pixmaps/%{oname}%{major}.png
install -D -m 0755 %{oname} %{buildroot}%{_libdir}/%{oname}%{major}/%{oname}
install -D -m 0644 keycodes.lst %{buildroot}%{_libdir}/%{oname}%{major}/keycodes.lst
cp -r cfg %{buildroot}%{_libdir}/%{oname}%{major}/
cp -r docs %{buildroot}%{_libdir}/%{oname}%{major}/
cp -r extra %{buildroot}%{_libdir}/%{oname}%{major}/
cp -r plugins %{buildroot}%{_libdir}/%{oname}%{major}/
cp -r shaders %{buildroot}%{_libdir}/%{oname}%{major}/

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{oname}%{major}.desktop << EOF
[Desktop Entry]
Name=ePSXe (%{major})
Comment=Sony PlayStation Emulator
Exec=/usr/bin/%{oname}%{major}-start
Icon=%{oname}%{major}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%{_bindir}/%{oname}%{major}-start
%{_libdir}/%{oname}%{major}/*
%{_datadir}/applications/%{oname}%{major}.desktop
%{_datadir}/pixmaps/%{oname}%{major}.png

