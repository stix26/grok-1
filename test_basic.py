"""
Basic tests for Grok-1 model components.
"""

import unittest
import os
import sys


class TestBasicFunctionality(unittest.TestCase):
    """Basic functionality tests for Grok-1."""

    def test_import_model(self):
        """Test that model components can be imported."""
        try:
            from model import LanguageModelConfig, TransformerConfig
            self.assertTrue(True, "Model imports successful")
        except ImportError as e:
            self.fail(f"Failed to import model components: {e}")

    def test_import_runners(self):
        """Test that runner components can be imported."""
        try:
            from runners import InferenceRunner, ModelRunner, sample_from_model
            self.assertTrue(True, "Runner imports successful")
        except ImportError as e:
            self.fail(f"Failed to import runner components: {e}")

    def test_import_checkpoint(self):
        """Test that checkpoint module can be imported."""
        try:
            import checkpoint
            self.assertTrue(True, "Checkpoint import successful")
        except ImportError as e:
            self.fail(f"Failed to import checkpoint module: {e}")

    def test_required_files_exist(self):
        """Test that all required files exist."""
        required_files = [
            'model.py',
            'runners.py',
            'run.py',
            'checkpoint.py',
            'requirements.txt',
            'README.md',
            'LICENSE.txt',
            'tokenizer.model'
        ]
        
        for file in required_files:
            with self.subTest(file=file):
                self.assertTrue(
                    os.path.exists(file), 
                    f"Required file {file} not found"
                )

    def test_python_version(self):
        """Test that we're using a compatible Python version."""
        version = sys.version_info
        self.assertGreaterEqual(version.major, 3, "Python 3+ required")
        self.assertGreaterEqual(version.minor, 9, "Python 3.9+ required")

    def test_working_directory(self):
        """Test that we're in the correct working directory."""
        self.assertTrue(
            os.path.exists('model.py'),
            "Should be in the grok-1 project directory"
        )


class TestModelConfiguration(unittest.TestCase):
    """Tests for model configuration."""

    def test_language_model_config_creation(self):
        """Test creating a LanguageModelConfig."""
        try:
            from model import LanguageModelConfig, TransformerConfig
            
            config = LanguageModelConfig(
                vocab_size=128 * 1024,
                pad_token=0,
                eos_token=2,
                sequence_len=8192,
                embedding_init_scale=1.0,
                output_multiplier_scale=0.5773502691896257,
                embedding_multiplier_scale=78.38367176906169,
                model=TransformerConfig(
                    emb_size=48 * 128,
                    widening_factor=8,
                    key_size=128,
                    num_q_heads=48,
                    num_kv_heads=8,
                    num_layers=64,
                    attn_output_multiplier=0.08838834764831845,
                    shard_activations=True,
                    num_experts=8,
                    num_selected_experts=2,
                    data_axis="data",
                    model_axis="model",
                ),
            )
            self.assertIsNotNone(config)
            self.assertEqual(config.vocab_size, 128 * 1024)
            self.assertEqual(config.sequence_len, 8192)
        except Exception as e:
            self.fail(f"Failed to create LanguageModelConfig: {e}")

    def test_transformer_config_creation(self):
        """Test creating a TransformerConfig."""
        try:
            from model import TransformerConfig
            
            config = TransformerConfig(
                emb_size=48 * 128,
                widening_factor=8,
                key_size=128,
                num_q_heads=48,
                num_kv_heads=8,
                num_layers=64,
                attn_output_multiplier=0.08838834764831845,
                shard_activations=True,
                num_experts=8,
                num_selected_experts=2,
                data_axis="data",
                model_axis="model",
            )
            self.assertIsNotNone(config)
            self.assertEqual(config.emb_size, 48 * 128)
            self.assertEqual(config.num_layers, 64)
            self.assertEqual(config.num_experts, 8)
        except Exception as e:
            self.fail(f"Failed to create TransformerConfig: {e}")


if __name__ == '__main__':
    unittest.main() 