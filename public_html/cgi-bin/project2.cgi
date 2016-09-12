#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "";

use CGI;
my $q = CGI->new();
my $a = $q->param('url');

print $a;

$page = `/usr/bin/curl http://$a`;

print $page;
