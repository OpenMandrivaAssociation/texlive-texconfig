# revision 27343
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texconfig
Version:	20121030
Release:	2
Summary:	TeXLive texconfig package
Group:		Publishing
URL:		http://tug.org/texlive
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
%{_texmfdir}/scripts/tetex/texconfig.sh
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/tetex/texconfig.sh texconfig
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 20121030-1
+ Revision: 820856
- Update to latest release.

* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812891
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756598
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719677
- texlive-texconfig
- texlive-texconfig
- texlive-texconfig
- texlive-texconfig

