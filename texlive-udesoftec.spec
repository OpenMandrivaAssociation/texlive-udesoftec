Name:		texlive-udesoftec
Version:	57866
Release:	1
Summary:	Thesis class for the University of Duisburg-Essen
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/udesoftec
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is designed for typesetting theses in the Research
Group for Business Informatics and Software Engineering. (The
class may also serve as a template for such theses.) The class
is designed for use with pdfLaTeX; input in UTF-8 encoding is
assumed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/udesoftec
%{_texmfdistdir}/tex/latex/udesoftec
%doc %{_texmfdistdir}/doc/latex/udesoftec
#- source
%doc %{_texmfdistdir}/source/latex/udesoftec

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
