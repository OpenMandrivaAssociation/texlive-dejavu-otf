Name:		texlive-dejavu-otf
Version:	45991
Release:	2
Summary:	Support for the ttf and otf DejaVu fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dejavu-otf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dejavu-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package dejavu-otf supports the free ttf-fonts from the DejaVu
project which are available from GitHub or already part of your
system (Windows/Linux/...) and the OpenType version of the
TeXGyre Math, which is part of any TeX distribution.. Following
font files are supported: DejaVuSans-BoldOblique.ttf
DejaVuSans-Bold.ttf DejaVuSansCondensed-BoldOblique.ttf
DejaVuSansCondensed-Bold.ttf DejaVuSansCondensed-Oblique.ttf
DejaVuSansCondensed.ttf DejaVuSans-ExtraLight.ttf
DejaVuSansMono-BoldOblique.ttf DejaVuSansMono-Bold.ttf
DejaVuSansMono-Oblique.ttf DejaVuSansMono.ttf
DejaVuSans-Oblique.ttf DejaVuSans.ttf
DejaVuSerif-BoldItalic.ttf DejaVuSerif-Bold.ttf
DejaVuSerifCondensed-BoldItalic.ttf
DejaVuSerifCondensed-Bold.ttf DejaVuSerifCondensed-Italic.ttf
DejaVuSerifCondensed.ttf DejaVuSerif-Italic.ttf DejaVuSerif.ttf
texgyredejavu-math.otf

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dejavu-otf
%doc %{_texmfdistdir}/doc/fonts/dejavu-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
