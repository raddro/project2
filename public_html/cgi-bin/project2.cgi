#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "";

use CGI;
my $q = CGI->new();
my $a = $q->param('url');

my $page = `/usr/bin/curl $a`;

$page=~s/</\&lt/g;
$page=~s/>/\&gt/g;

print $page;
