# installs the package puppet-lint
package { 'puppet-lint':
ensure    => '2.2.3',
provider  => 'gem',
}
