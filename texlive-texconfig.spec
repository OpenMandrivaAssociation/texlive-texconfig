# revision 33736
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texconfig
Version:	20140621
Release:	6
Summary:	TeXLive texconfig package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texconfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texconfig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texconfig.bin = %{EVRD}

%description
TeXLive texconfig package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texconfig
%{_texmfdistdir}/scripts/texlive/texconfig.sh
%{_texmfdistdir}/texconfig/README
%{_texmfdistdir}/texconfig/g/generic
%{_texmfdistdir}/texconfig/tcfmgr
%{_texmfdistdir}/texconfig/tcfmgr.map
%{_texmfdistdir}/texconfig/v/vt100
%{_texmfdistdir}/texconfig/x/xterm
%doc %{_mandir}/man1/texconfig-sys.1*
%doc %{_texmfdistdir}/doc/man/man1/texconfig-sys.man1.pdf
%doc %{_mandir}/man1/texconfig.1*
%doc %{_texmfdistdir}/doc/man/man1/texconfig.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texlive/texconfig.sh texconfig
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
