#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Deriv
Version  : 4.1.3
Release  : 36
URL      : https://cran.r-project.org/src/contrib/Deriv_4.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Deriv_4.1.3.tar.gz
Summary  : Symbolic Differentiation
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
user-defined function as well as function substitution
    in arguments of functions to be differentiated. Some symbolic
    simplification is part of the work.

%prep
%setup -q -c -n Deriv
cd %{_builddir}/Deriv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640998965

%install
export SOURCE_DATE_EPOCH=1640998965
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Deriv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Deriv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Deriv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Deriv || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Deriv/CITATION
/usr/lib64/R/library/Deriv/DESCRIPTION
/usr/lib64/R/library/Deriv/INDEX
/usr/lib64/R/library/Deriv/Meta/Rd.rds
/usr/lib64/R/library/Deriv/Meta/features.rds
/usr/lib64/R/library/Deriv/Meta/hsearch.rds
/usr/lib64/R/library/Deriv/Meta/links.rds
/usr/lib64/R/library/Deriv/Meta/nsInfo.rds
/usr/lib64/R/library/Deriv/Meta/package.rds
/usr/lib64/R/library/Deriv/NAMESPACE
/usr/lib64/R/library/Deriv/NEWS
/usr/lib64/R/library/Deriv/R/Deriv
/usr/lib64/R/library/Deriv/R/Deriv.rdb
/usr/lib64/R/library/Deriv/R/Deriv.rdx
/usr/lib64/R/library/Deriv/help/AnIndex
/usr/lib64/R/library/Deriv/help/Deriv.rdb
/usr/lib64/R/library/Deriv/help/Deriv.rdx
/usr/lib64/R/library/Deriv/help/aliases.rds
/usr/lib64/R/library/Deriv/help/paths.rds
/usr/lib64/R/library/Deriv/html/00Index.html
/usr/lib64/R/library/Deriv/html/R.css
/usr/lib64/R/library/Deriv/tests/testthat.R
/usr/lib64/R/library/Deriv/tests/testthat/test_Deriv.R
/usr/lib64/R/library/Deriv/tests/testthat/test_Simplify.R
