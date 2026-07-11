%global tl_name udesoftec
%global tl_revision 57866

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7.1
Release:	%{tl_revision}.1
Summary:	Thesis class for the University of Duisburg-Essen
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/udesoftec
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/udesoftec.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is designed for typesetting theses in the Research Group for
Business Informatics and Software Engineering. (The class may also serve
as a template for such theses.) The class is designed for use with
pdfLaTeX; input in UTF-8 encoding is assumed.

