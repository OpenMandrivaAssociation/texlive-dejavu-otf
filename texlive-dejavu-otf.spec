%global tl_name dejavu-otf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.07
Release:	%{tl_revision}.1
Summary:	Support for the ttf and otf DejaVu fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dejavu-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package supports the free ttf-fonts from the DejaVu project which
are available from GitHub or already part of your system
(Windows/Linux/...), and the OpenType version of TeXGyre Math, which is
part of any TeX distribution. The following font files are supported:
DejaVuSans-BoldOblique.ttf DejaVuSans-Bold.ttf DejaVuSansCondensed-
BoldOblique.ttf DejaVuSansCondensed-Bold.ttf DejaVuSansCondensed-
Oblique.ttf DejaVuSansCondensed.ttf DejaVuSans-ExtraLight.ttf
DejaVuSansMono-BoldOblique.ttf DejaVuSansMono-Bold.ttf DejaVuSansMono-
Oblique.ttf DejaVuSansMono.ttf DejaVuSans-Oblique.ttf DejaVuSans.ttf
DejaVuSerif-BoldItalic.ttf DejaVuSerif-Bold.ttf DejaVuSerifCondensed-
BoldItalic.ttf DejaVuSerifCondensed-Bold.ttf DejaVuSerifCondensed-
Italic.ttf DejaVuSerifCondensed.ttf DejaVuSerif-Italic.ttf
DejaVuSerif.ttf texgyredejavu-math.otf

