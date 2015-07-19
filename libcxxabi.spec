Summary:	C++ Standard Library
Name:		libcxxabi
Version:	3.5.1
Release:	2
License:	MIT
Group:		System/Libraries
URL:		http://libcxxabi.llvm.org/
Source0:	http://llvm.org/releases/%{name}/%{name}-%{version}.src.tar.xz
BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:	llvm-devel

%track
prog %{name} = {
	url = http://llvm.org/releases/%{version}/
	regex = "%{name}-(__VER__)\.tar\.xz"
	version = %{version}
}

%description
libc++abi is a new implementation of low level
support for a standard C++ library.

%prep
%setup -qn %{name}-%{version}.src

%build
pushd lib
./buildit
popd

%install
%makeinstall_std

%files
%doc LICENSE.TXT CREDITS.TXT
