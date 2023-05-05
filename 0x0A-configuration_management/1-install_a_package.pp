# installs the package puppet-lint
package { 'puppet-lint':
ensure   => '4.0.0',
provider => 'gem',
}
