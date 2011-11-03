# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texconfig
Version:	20111103
Release:	1
Summary:	TeXLive texconfig package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texconfig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texconfig.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texconfig.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-texconfig.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive texconfig package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texconfig
%{_texmfdir}/texconfig/README
%{_texmfdir}/texconfig/g/generic
%{_texmfdir}/texconfig/tcfmgr
%{_texmfdir}/texconfig/tcfmgr.map
%{_texmfdir}/texconfig/v/vt100
%{_texmfdir}/texconfig/x/xterm
%doc %{_mandir}/man1/texconfig-sys.1*
%doc %{_texmfdir}/doc/man/man1/texconfig-sys.man1.pdf
%doc %{_mandir}/man1/texconfig.1*
%doc %{_texmfdir}/doc/man/man1/texconfig.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
# shell script
mkdir -p %{buildroot}%{_bindir}
cp -fpa bin/x86_64-linux/texconfig %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
