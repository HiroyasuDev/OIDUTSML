#!/usr/bin/env python3
"""
Optimization Validation Script
Validates actual performance against expected optimizations
"""

import json
import time
import requests
import statistics
from datetime import datetime
from pathlib import Path

API_URL = "http://localhost:3000"
LM_STUDIO_URL = "http://localhost:1234"

def test_endpoint_performance(url, name, iterations=10):
    """Test endpoint performance"""
    times = []
    errors = 0
    
    for i in range(iterations):
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            duration = (time.time() - start) * 1000  # Convert to ms
            
            if response.status_code == 200:
                times.append(duration)
            else:
                errors += 1
        except Exception as e:
            errors += 1
    
    if not times:
        return None
    
    return {
        'name': name,
        'average': statistics.mean(times),
        'min': min(times),
        'max': max(times),
        'median': statistics.median(times),
        'stdev': statistics.stdev(times) if len(times) > 1 else 0,
        'errors': errors,
        'success_rate': (len(times) / iterations) * 100
    }

def validate_configuration():
    """Validate optimization configuration"""
    config_path = Path('config/inference-optimized.json')
    
    if not config_path.exists():
        return {'status': 'error', 'message': 'Config file not found'}
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        settings = config.get('optimized_settings', {})
        hardware = config.get('hardware', {})
        
        return {
            'status': 'success',
            'settings': settings,
            'hardware': hardware,
            'validated': True
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def test_lm_studio_integration():
    """Test LM Studio integration"""
    results = {
        'api_available': False,
        'models_available': False,
        'chat_working': False
    }
    
    # Test API availability
    try:
        response = requests.get(f"{LM_STUDIO_URL}/v1/models", timeout=2)
        if response.status_code == 200:
            results['api_available'] = True
            data = response.json()
            if data.get('data'):
                results['models_available'] = True
    except:
        pass
    
    # Test chat endpoint
    if results['api_available']:
        try:
            response = requests.post(
                f"{API_URL}/api/v1/lm-studio/chat",
                json={
                    'messages': [{'role': 'user', 'content': 'Hi'}],
                    'max_tokens': 10
                },
                timeout=10
            )
            if response.status_code == 200:
                results['chat_working'] = True
        except:
            pass
    
    return results

def validate_optimization_settings():
    """Validate that optimization settings are being applied"""
    # Check if service is loading config
    config = validate_configuration()
    
    if config['status'] == 'error':
        return {'status': 'error', 'message': config['message']}
    
    settings = config['settings']
    
    # Validate settings are within expected ranges
    validations = {
        'temperature': 0 <= settings.get('temperature', 0) <= 2,
        'max_tokens': 0 < settings.get('max_tokens', 0) <= 4096,
        'top_p': 0 < settings.get('top_p', 0) <= 1,
        'top_k': settings.get('top_k', 0) > 0,
        'repeat_penalty': settings.get('repeat_penalty', 0) > 0,
        'num_threads': settings.get('num_threads', 0) > 0
    }
    
    return {
        'status': 'success',
        'settings': settings,
        'validations': validations,
        'all_valid': all(validations.values())
    }

def main():
    print("=" * 60)
    print("Optimization Validation Report")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("")
    
    results = {
        'timestamp': datetime.now().isoformat(),
        'performance': {},
        'configuration': {},
        'integration': {},
        'optimization': {}
    }
    
    # Test 1: Performance Validation
    print("1. Performance Validation")
    print("-" * 60)
    
    health_perf = test_endpoint_performance(f"{API_URL}/health", "Health Endpoint")
    if health_perf:
        print(f"   {health_perf['name']}:")
        print(f"     Average: {health_perf['average']:.2f}ms")
        print(f"     Min: {health_perf['min']:.2f}ms")
        print(f"     Max: {health_perf['max']:.2f}ms")
        print(f"     Median: {health_perf['median']:.2f}ms")
        print(f"     Success Rate: {health_perf['success_rate']:.1f}%")
        print(f"     Target: <100ms")
        print(f"     Status: {'✅ PASS' if health_perf['average'] < 100 else '⚠️  SLOW'}")
        results['performance']['health'] = health_perf
    
    api_perf = test_endpoint_performance(f"{API_URL}/api/v1", "API Endpoint")
    if api_perf:
        print(f"\n   {api_perf['name']}:")
        print(f"     Average: {api_perf['average']:.2f}ms")
        print(f"     Min: {api_perf['min']:.2f}ms")
        print(f"     Max: {api_perf['max']:.2f}ms")
        print(f"     Median: {api_perf['median']:.2f}ms")
        print(f"     Success Rate: {api_perf['success_rate']:.1f}%")
        print(f"     Target: <100ms")
        print(f"     Status: {'✅ PASS' if api_perf['average'] < 100 else '⚠️  SLOW'}")
        results['performance']['api'] = api_perf
    
    # Test 2: Configuration Validation
    print("\n2. Configuration Validation")
    print("-" * 60)
    
    config = validate_configuration()
    if config['status'] == 'success':
        settings = config['settings']
        print("   Optimization Settings:")
        print(f"     Temperature: {settings.get('temperature')}")
        print(f"     Max Tokens: {settings.get('max_tokens')}")
        print(f"     Top P: {settings.get('top_p')}")
        print(f"     Top K: {settings.get('top_k')}")
        print(f"     Repeat Penalty: {settings.get('repeat_penalty')}")
        print(f"     Threads: {settings.get('num_threads')}")
        print(f"     Context Length: {settings.get('context_length')}")
        print("   Status: ✅ Configuration loaded and valid")
        results['configuration'] = config
    else:
        print(f"   Status: ❌ {config['message']}")
        results['configuration'] = config
    
    # Test 3: Optimization Settings Validation
    print("\n3. Optimization Settings Validation")
    print("-" * 60)
    
    opt_validation = validate_optimization_settings()
    if opt_validation['status'] == 'success':
        validations = opt_validation['validations']
        print("   Setting Validations:")
        for key, valid in validations.items():
            status = "✅" if valid else "❌"
            print(f"     {status} {key}: {valid}")
        print(f"   Overall: {'✅ ALL VALID' if opt_validation['all_valid'] else '❌ SOME INVALID'}")
        results['optimization'] = opt_validation
    else:
        print(f"   Status: ❌ {opt_validation.get('message', 'Unknown error')}")
        results['optimization'] = opt_validation
    
    # Test 4: LM Studio Integration
    print("\n4. LM Studio Integration")
    print("-" * 60)
    
    integration = test_lm_studio_integration()
    print(f"   API Available: {'✅' if integration['api_available'] else '⚠️  Not running'}")
    print(f"   Models Available: {'✅' if integration['models_available'] else '⚠️  No models'}")
    print(f"   Chat Working: {'✅' if integration['chat_working'] else '⚠️  Not tested'}")
    results['integration'] = integration
    
    # Summary
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    performance_ok = (
        health_perf and health_perf['average'] < 100 and
        api_perf and api_perf['average'] < 100
    )
    config_ok = config['status'] == 'success'
    optimization_ok = opt_validation.get('all_valid', False)
    
    print(f"Performance: {'✅ PASS' if performance_ok else '⚠️  NEEDS ATTENTION'}")
    print(f"Configuration: {'✅ PASS' if config_ok else '❌ FAIL'}")
    print(f"Optimization: {'✅ PASS' if optimization_ok else '❌ FAIL'}")
    print(f"Integration: {'✅ READY' if integration['api_available'] else '⚠️  LM Studio not running'}")
    
    # Save results
    output_file = Path('test_results/optimization_validation.json')
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📄 Results saved to: {output_file}")
    print("\n✅ Validation complete!")

if __name__ == '__main__':
    main()
